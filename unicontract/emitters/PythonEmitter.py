import os
import io
from typing import Dict
from unicontract.elements.Elements import *
from unicontract.Engine import *


def DoEmit(session: Session, output_dir: str, configuration: Dict[str, str]):
    """
    Creates a PythonEmitter, emits one module per namespace and writes them to disk.
    """
    emitter = PythonEmitter(output_dir, configuration)
    results: List[python_code] = emitter.Emit(session)

    for code in results:
        dir_name = os.path.dirname(code.fullPath)
        if dir_name and not os.path.exists(dir_name):
            os.makedirs(dir_name)
        with open(code.fullPath, "w") as file:
            file.write(code.content)

    return results


class PythonEmitter:
    def __init__(self, output_dir: str = "./", configuration: Dict[str, str] = {}):
        self.configuration: python_configuration = python_configuration(configuration, output_dir)

    def Emit(self, session: Session):
        """
        A Python module is a namespace, so every namespace becomes one <name>.py file holding all
        of its enums and interfaces.
        """
        result: List[python_code] = []

        for namespace in session.main.namespaces:
            path: str = self.configuration.output_dir
            if self.configuration.createFolderStructure and len(namespace.name.names) > 1:
                path = os.path.join(self.configuration.output_dir, *namespace.name.names[:-1])
            module_name = namespace.name.names[-1]

            content: str = self.beginFile(namespace, session)
            for enum in namespace.enums:
                content += self.enumText(enum)
            for interface in namespace.interfaces:
                content += self.interfaceText(interface)
            result.append(python_code(path, module_name, content))

        return result

    def fileHeader(self) -> str:
        return self.configuration.fileHeader

    def defaultImports(self) -> str:
        return "".join(f"{imp}\n" for imp in self.configuration.defaultImports)

    def importsText(self, current_namespace: namespace, session: Session) -> str:
        """
        A contract 'import' of another namespace becomes 'from <namespace> import *'.
        """
        buffer = io.StringIO()
        for _import in session.main.imports:
            if _import.contract is None:
                continue
            for imported_namespace in _import.contract.namespaces:
                if imported_namespace.name.getText() != current_namespace.name.getText():
                    buffer.write(f"from {imported_namespace.name.names[-1]} import *\n")
        return buffer.getvalue()

    def beginFile(self, namespace: namespace, session: Session) -> str:
        buffer = io.StringIO()
        buffer.write(self.fileHeader())
        buffer.write("\n")
        buffer.write(self.defaultImports())
        buffer.write(self.importsText(namespace, session))
        return buffer.getvalue()

    def documentLines(self, hinted_element: hinted_base_element, indent: int = 0) -> str:
        buffer = io.StringIO()
        for document_line in hinted_element.document_lines:
            buffer.write(f"{self.tab(indent)}#{document_line}\n")
        return buffer.getvalue()

    def enumText(self, enum: enum, indent: int = 0) -> str:
        buffer = io.StringIO()
        buffer.write("\n\n")
        buffer.write(self.documentLines(enum, indent))
        buffer.write(f"{self.tab(indent)}class {enum.name}(Enum):\n")
        if len(enum.enum_elements) == 0:
            buffer.write(f"{self.tab(indent + 1)}pass\n")
        for enum_element in enum.enum_elements:
            buffer.write(self.documentLines(enum_element, indent + 1))
            buffer.write(f'{self.tab(indent + 1)}{enum_element.value} = "{enum_element.value}"\n')
        return buffer.getvalue()

    def interfaceText(self, interface: interface, indent: int = 0) -> str:
        buffer = io.StringIO()
        buffer.write("\n\n")

        # TypeVars for the interface's own generic parameters (constraints -> bound)
        if interface.generic:
            buffer.write(self.typeVarDeclarations(interface.generic, indent))

        buffer.write(self.documentLines(interface, indent))

        # base classes: inherited interfaces (+ Generic[...]) or ABC
        bases: List[str] = []
        for inherit in interface.inherits:
            base = inherit.reference_name.getText()
            if inherit.generic:
                base += f"[{self.genericArgs(inherit.generic)}]"
            bases.append(base)
        if len(bases) == 0:
            bases.append("ABC")
        if interface.generic:
            bases.append(f"Generic[{self.genericArgs(interface.generic)}]")

        buffer.write(f"{self.tab(indent)}class {interface.name}({', '.join(bases)}):\n")

        body = io.StringIO()
        for enum in interface.enums:
            body.write(self.enumText(enum, indent + 1))
        for property in interface.properties:
            body.write(self.propertyText(property, indent + 1))
        for method in interface.methods:
            body.write(self.methodText(method, indent + 1))

        body_text = body.getvalue()
        if body_text.strip() == "":
            buffer.write(f"{self.tab(indent + 1)}pass\n")
        else:
            buffer.write(body_text)
        return buffer.getvalue()

    def propertyText(self, property: interface_property, indent: int) -> str:
        """
        A contract property becomes an abstract @property getter (and a setter unless readonly).
        """
        buffer = io.StringIO()
        type_text = self.typeText(property.type)
        buffer.write("\n")
        buffer.write(self.documentLines(property, indent))
        buffer.write(f"{self.tab(indent)}@property\n")
        buffer.write(f"{self.tab(indent)}@abstractmethod\n")
        buffer.write(f"{self.tab(indent)}def {property.name}(self) -> {type_text}:\n")
        buffer.write(f"{self.tab(indent + 1)}...\n")
        if not property.isReadonly:
            buffer.write(f"{self.tab(indent)}@{property.name}.setter\n")
            buffer.write(f"{self.tab(indent)}@abstractmethod\n")
            buffer.write(f"{self.tab(indent)}def {property.name}(self, value: {type_text}) -> None:\n")
            buffer.write(f"{self.tab(indent + 1)}...\n")
        return buffer.getvalue()

    def methodText(self, method: interface_method, indent: int) -> str:
        buffer = io.StringIO()
        buffer.write("\n")
        buffer.write(self.documentLines(method, indent))

        # TypeVars for a generic method's own parameters
        if method.generic:
            buffer.write(self.typeVarDeclarations(method.generic, indent))

        buffer.write(self.tab(indent))
        buffer.write("@abstractmethod\n")
        buffer.write(self.tab(indent))
        buffer.write("async def " if method.isAsync else "def ")
        buffer.write(f"{method.name}(self")
        for param in method.params:
            buffer.write(f", {param.name}: {self.typeText(param.type)}")
        buffer.write(")")

        return_text = self.typeText(method.return_type) if method.return_type is not None else "None"
        buffer.write(f" -> {return_text}:\n")
        buffer.write(f"{self.tab(indent + 1)}...\n")
        return buffer.getvalue()

    def typeVarDeclarations(self, generic: generic, indent: int) -> str:
        buffer = io.StringIO()
        for generic_type in generic.types:
            if generic_type.constraint is not None:
                # a string bound is a lazy forward reference, so no import is required
                buffer.write(f'{self.tab(indent)}{generic_type.type_name} = TypeVar("{generic_type.type_name}", bound="{generic_type.constraint.getText()}")\n')
            else:
                buffer.write(f'{self.tab(indent)}{generic_type.type_name} = TypeVar("{generic_type.type_name}")\n')
        return buffer.getvalue()

    def genericArgs(self, generic: generic) -> str:
        return ", ".join(generic_type.type_name for generic_type in generic.types)

    def typeText(self, type: type) -> str:
        match type.kind:
            case type.Kind.Primitive:
                return self.typeTextPrimitive(type)
            case type.Kind.Reference:
                return self.typeTextReference(type)
            case type.Kind.List:
                return self.typeTextList(type)
            case type.Kind.Map:
                return self.typeTextMap(type)
            case type.Kind.Query:
                return self.typeTextQuery(type)

    def typeTextPrimitive(self, type: primitive_type) -> str:
        match type.primtiveKind:
            case primitive_type.PrimtiveKind.Any:
                return "Any"
            case primitive_type.PrimtiveKind.Integer:
                return "int"
            case primitive_type.PrimtiveKind.Number:
                return "Decimal"
            case primitive_type.PrimtiveKind.Float:
                return "float"
            case primitive_type.PrimtiveKind.Date:
                return "date"
            case primitive_type.PrimtiveKind.Time:
                return "time"
            case primitive_type.PrimtiveKind.DateTime:
                return "datetime"
            case primitive_type.PrimtiveKind.String:
                return "str"
            case primitive_type.PrimtiveKind.Boolean:
                return "bool"
            case primitive_type.PrimtiveKind.Bytes:
                return "bytes"
            case primitive_type.PrimtiveKind.Stream:
                return "BinaryIO"

    def typeTextReference(self, reference_type: reference_type) -> str:
        buffer = io.StringIO()
        buffer.write(reference_type.reference_name.getText())
        if reference_type.generic is not None:
            buffer.write(f"[{self.genericArgs(reference_type.generic)}]")
        return buffer.getvalue()

    def typeTextQuery(self, query_type: query_type) -> str:
        return f"Iterable[{self.genericArgs(query_type.generic)}]"

    def typeTextList(self, type: list_type) -> str:
        return f"List[{self.typeText(type.item_type)}]"

    def typeTextMap(self, type: map_type) -> str:
        return f"Dict[{self.typeText(type.key_type)}, {self.typeText(type.value_type)}]"

    def tab(self, indent=1) -> str:
        return '    ' * indent


class python_configuration:
    def __init__(self, configuration: Dict[str, str], output_dir: str):
        self.output_dir = output_dir
        self.__read_fileHeader(configuration)
        self.__read_defaultImports(configuration)
        self.__read_createFolderStructure(configuration)

    def __read_fileHeader(self, configuration: Dict[str, str]):
        self.fileHeader: str = """# <auto-generated>
#     This code was generated by unicontract
#     see more information: https://github.com/gyorgy-gulyas/UniContract
#
#     Changes to this file may cause incorrect behavior and will be lost if the code is regenerated.
# </auto-generated>"""
        if "python.file_header_lines" in configuration:
            value = configuration["python.file_header_lines"]
            if isinstance(value, list) and all(isinstance(item, str) for item in value):
                self.fileHeader = "\n".join(value)

    def __read_defaultImports(self, configuration: Dict[str, str]):
        self.defaultImports: List[str] = [
            "from __future__ import annotations",
            "from abc import ABC, abstractmethod",
            "from enum import Enum",
            "from typing import Any, List, Dict, Optional, Generic, TypeVar, BinaryIO",
            "from decimal import Decimal",
            "from datetime import date, time, datetime",
        ]
        if "python.default_imports" in configuration:
            value = configuration["python.default_imports"]
            if isinstance(value, list) and all(isinstance(item, str) for item in value):
                self.defaultImports = value

    def __read_createFolderStructure(self, configuration: Dict[str, str]):
        self.createFolderStructure: bool = True
        if "python.create_folder_structure" in configuration:
            self.createFolderStructure = bool(configuration["python.create_folder_structure"])


class python_code:
    def __init__(self, directory: str, name: str, content: str):
        self.fileName: str = name + ".py"
        self.fullPath: str = os.path.join(directory, self.fileName)
        self.content: str = content


if __name__ == "__main__":
    pass
