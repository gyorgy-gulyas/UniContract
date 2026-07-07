import os
import io
from typing import Dict
from unicontract.elements.Elements import *
from unicontract.Engine import *


def DoEmit(session: Session, output_dir: str, configuration: Dict[str, str]):
    """
    Creates a JavaEmitter, emits the Java interfaces/enums for the session and writes them to disk.
    """
    emitter = JavaEmitter(output_dir, configuration)
    results: List[java_code] = emitter.Emit(session)

    for code in results:
        dir_name = os.path.dirname(code.fullPath)
        if dir_name and not os.path.exists(dir_name):
            os.makedirs(dir_name)
        with open(code.fullPath, "w") as file:
            file.write(code.content)

    return results


class JavaEmitter:
    def __init__(self, output_dir: str = "./", configuration: Dict[str, str] = {}):
        self.configuration: java_configuration = java_configuration(configuration, output_dir)

    def Emit(self, session: Session):
        """
        Emits one .java file per top-level enum and interface (Java allows one public type per file).
        """
        result: List[java_code] = []

        for namespace in session.main.namespaces:
            path: str = self.configuration.output_dir
            if self.configuration.createFolderStructure:
                path = os.path.join(self.configuration.output_dir, *namespace.name.names)

            for enum in namespace.enums:
                content: str = self.beginFile(namespace, session)
                content += self.enumText(enum, indent=0)
                content += self.endFile(namespace)
                result.append(java_code(path, enum.name, content))

            for interface in namespace.interfaces:
                content: str = self.beginFile(namespace, session)
                content += self.interfaceText(interface, indent=0)
                content += self.endFile(namespace)
                result.append(java_code(path, interface.name, content))

        return result

    def fileHeader(self) -> str:
        return self.configuration.fileHeader

    def defaultImports(self) -> str:
        return "".join(f"import {imp};\n" for imp in self.configuration.defaultImports)

    def importsText(self, current_namespace: namespace, session: Session) -> str:
        """
        A contract 'import' of another namespace becomes a Java 'import <namespace>.*;'.
        """
        buffer = io.StringIO()
        for _import in session.main.imports:
            if _import.contract is None:
                continue
            for imported_namespace in _import.contract.namespaces:
                if imported_namespace.name.getText() != current_namespace.name.getText():
                    buffer.write(f"import {imported_namespace.name.getText()}.*;\n")
        return buffer.getvalue()

    def beginFile(self, namespace: namespace, session: Session) -> str:
        buffer = io.StringIO()
        buffer.write(self.fileHeader())
        buffer.write("\n")
        buffer.write(f"package {namespace.name.getText()};\n\n")
        buffer.write(self.defaultImports())
        buffer.write(self.importsText(namespace, session))
        buffer.write("\n")
        return buffer.getvalue()

    def endFile(self, namespace: namespace) -> str:
        return "\n"

    def documentLines(self, hinted_element: hinted_base_element, indent: int = 0) -> str:
        buffer = io.StringIO()
        for document_line in hinted_element.document_lines:
            buffer.write(f"{self.tab(indent)}//{document_line}\n")
        return buffer.getvalue()

    def enumText(self, enum: enum, indent: int = 0) -> str:
        buffer = io.StringIO()
        buffer.write("\n")
        buffer.write(self.documentLines(enum, indent))
        buffer.write(f"{self.tab(indent)}public enum {enum.name} {{\n")
        for enum_element in enum.enum_elements:
            buffer.write(self.documentLines(enum_element, indent + 1))
            buffer.write(f"{self.tab(indent + 1)}{enum_element.value},\n")
        buffer.write(f"{self.tab(indent)}}}\n")
        return buffer.getvalue()

    def interfaceText(self, interface: interface, indent: int = 0) -> str:
        buffer = io.StringIO()
        buffer.write(self.documentLines(interface, indent))
        buffer.write(f"{self.tab(indent)}public interface {interface.name}")

        # generic declaration (constraints are inline in Java: <T extends X>)
        if interface.generic:
            buffer.write(self.genericText(interface.generic))

        # inheritance: Java interfaces 'extend' other interfaces
        firstInherit: bool = True
        for inherit in interface.inherits:
            buffer.write(" extends " if firstInherit else ", ")
            firstInherit = False
            buffer.write(inherit.reference_name.getText())
            if inherit.generic:
                buffer.write(self.genericText(inherit.generic))

        buffer.write(" {\n")

        # nested enums
        for enum in interface.enums:
            buffer.write(self.enumText(enum, indent + 1))
        if len(interface.enums) > 0 and len(interface.properties) > 0:
            buffer.write("\n")

        # properties -> getter (+ setter unless readonly)
        for property in interface.properties:
            buffer.write(self.propertyText(property, indent + 1))
        if (len(interface.enums) > 0 or len(interface.properties) > 0) and len(interface.methods) > 0:
            buffer.write("\n")

        # methods
        for method in interface.methods:
            buffer.write(self.methodText(method, indent + 1))

        buffer.write(f"{self.tab(indent)}}}")
        return buffer.getvalue()

    def propertyText(self, property: interface_property, indent: int) -> str:
        """
        Java interfaces have no properties; a contract property becomes a getter (and, unless
        readonly, a setter).
        """
        buffer = io.StringIO()
        buffer.write(self.documentLines(property, indent))
        type_text = self.typeText(property.type)
        cap = property.name[0].upper() + property.name[1:]
        buffer.write(f"{self.tab(indent)}{type_text} get{cap}();\n")
        if not property.isReadonly:
            buffer.write(f"{self.tab(indent)}void set{cap}({type_text} value);\n")
        return buffer.getvalue()

    def methodText(self, method: interface_method, indent: int) -> str:
        buffer = io.StringIO()
        buffer.write(self.documentLines(method, indent))
        buffer.write(self.tab(indent))

        # in Java the generic parameter list comes BEFORE the return type
        if method.generic:
            buffer.write(self.genericText(method.generic))
            buffer.write(" ")

        # return type; async maps to CompletableFuture<T> (boxed argument)
        if method.return_type is not None:
            if method.isAsync:
                buffer.write(f"CompletableFuture<{self.typeText(method.return_type, boxed=True)}>")
            else:
                buffer.write(self.typeText(method.return_type))
        else:
            buffer.write("CompletableFuture<Void>" if method.isAsync else "void")

        buffer.write(f" {method.name}(")

        break_lines = any(param.document_lines for param in method.params) or len(method.params) >= 5
        firstParam: bool = True
        for param in method.params:
            if not firstParam:
                buffer.write("," if break_lines else ", ")
            if break_lines:
                buffer.write("\n")
                buffer.write(self.documentLines(param, indent + 1))
                buffer.write(self.tab(indent + 1))
            buffer.write(f"{self.typeText(param.type)} {param.name}")
            firstParam = False
        if break_lines and len(method.params) > 0:
            buffer.write("\n" + self.tab(indent))

        buffer.write(");\n")
        return buffer.getvalue()

    def genericText(self, generic: generic) -> str:
        """
        <T, U extends X>. A constraint is inline (Java has no 'where'); 'instantiable' (new())
        has no Java equivalent and is ignored.
        """
        buffer = io.StringIO()
        buffer.write("<")
        firstParam: bool = True
        for generic_type in generic.types:
            if not firstParam:
                buffer.write(", ")
            buffer.write(generic_type.type_name)
            if generic_type.constraint is not None:
                buffer.write(f" extends {generic_type.constraint.getText()}")
            firstParam = False
        buffer.write(">")
        return buffer.getvalue()

    def typeText(self, type: type, boxed: bool = False) -> str:
        match type.kind:
            case type.Kind.Primitive:
                return self.typeTextPrimitive(type, boxed)
            case type.Kind.Reference:
                return self.typeTextReference(type)
            case type.Kind.List:
                return self.typeTextList(type)
            case type.Kind.Map:
                return self.typeTextMap(type)

    def typeTextPrimitive(self, type: primitive_type, boxed: bool = False) -> str:
        # 'boxed' is used inside generics (List<Integer>, CompletableFuture<Boolean>, ...),
        # where Java forbids primitive type arguments.
        match type.primtiveKind:
            case primitive_type.PrimtiveKind.Any:
                return "Object"
            case primitive_type.PrimtiveKind.Integer:
                return "Integer" if boxed else "int"
            case primitive_type.PrimtiveKind.Number:
                return "BigDecimal"
            case primitive_type.PrimtiveKind.Float:
                return "Double" if boxed else "double"
            case primitive_type.PrimtiveKind.Date:
                return "LocalDate"
            case primitive_type.PrimtiveKind.Time:
                return "LocalTime"
            case primitive_type.PrimtiveKind.DateTime:
                return "LocalDateTime"
            case primitive_type.PrimtiveKind.String:
                return "String"
            case primitive_type.PrimtiveKind.Boolean:
                return "Boolean" if boxed else "boolean"
            case primitive_type.PrimtiveKind.Bytes:
                return "byte[]"
            case primitive_type.PrimtiveKind.Stream:
                return "InputStream"

    def typeTextReference(self, reference_type: reference_type) -> str:
        buffer = io.StringIO()
        buffer.write(reference_type.reference_name.getText())
        if reference_type.generic is not None:
            buffer.write(self.genericText(reference_type.generic))
        return buffer.getvalue()

    def typeTextList(self, type: list_type) -> str:
        return f"List<{self.typeText(type.item_type, boxed=True)}>"

    def typeTextMap(self, type: map_type) -> str:
        return f"Map<{self.typeText(type.key_type, boxed=True)}, {self.typeText(type.value_type, boxed=True)}>"

    def tab(self, indent=1) -> str:
        return '\t' * indent


class java_configuration:
    def __init__(self, configuration: Dict[str, str], output_dir: str):
        self.output_dir = output_dir
        self.__read_fileHeader(configuration)
        self.__read_defaultImports(configuration)
        self.__read_createFolderStructure(configuration)

    def __read_fileHeader(self, configuration: Dict[str, str]):
        self.fileHeader: str = """/*
 * <auto-generated>
 *     This code was generated by unicontract
 *     see more information: https://github.com/gyorgy-gulyas/UniContract
 *
 *     Changes to this file may cause incorrect behavior and will be lost if the code is regenerated.
 * </auto-generated>
 */"""
        if "java.file_header_lines" in configuration:
            value = configuration["java.file_header_lines"]
            if isinstance(value, list) and all(isinstance(item, str) for item in value):
                self.fileHeader = "\n".join(value)

    def __read_defaultImports(self, configuration: Dict[str, str]):
        self.defaultImports: List[str] = [
            "java.util.List",
            "java.util.Map",
            "java.util.concurrent.CompletableFuture",
            "java.math.BigDecimal",
            "java.time.LocalDate",
            "java.time.LocalTime",
            "java.time.LocalDateTime",
            "java.io.InputStream",
        ]
        if "java.default_imports" in configuration:
            value = configuration["java.default_imports"]
            if isinstance(value, list) and all(isinstance(item, str) for item in value):
                self.defaultImports = value

    def __read_createFolderStructure(self, configuration: Dict[str, str]):
        self.createFolderStructure: bool = True
        if "java.create_folder_structure" in configuration:
            self.createFolderStructure = bool(configuration["java.create_folder_structure"])


class java_code:
    def __init__(self, directory: str, name: str, content: str):
        self.fileName: str = name + ".java"
        self.fullPath: str = os.path.join(directory, self.fileName)
        self.content: str = content


if __name__ == "__main__":
    pass
