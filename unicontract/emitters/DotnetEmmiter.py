import os
import io
from typing import Dict
from unicontract.elements.Elements import *
from unicontract.Engine import *


def DoEmit(session: Session, output_dir: str, configuration: Dict[str, str]):
    dotnetEmmiter = DotnetEmmiter(output_dir, configuration)

    result: List[dotnet_code] = dotnetEmmiter.Emit(session)


class DotnetEmmiter:
    def __init__(self, output_dir: str ="./", configuration: Dict[str, str] ={}):
        self.configuration: dotnet_configuration = dotnet_configuration(configuration, output_dir)

    def Emit(self, session: Session):
        result: List[dotnet_code] = []

        for namespace in session.main.namespaces:
            path: str = self.configuration.output_dir
            if (self.configuration.createFolderStructure == True):
                path = os.path.join(self.configuration.output_dir, *namespace.name.names)

            for enum in namespace.enums:
                content: str = self.beginFile(namespace)
                content += self.enumText(enum, indent=1)
                content += self.endFile(namespace)
                result.append(dotnet_code(path, enum.name, content))

            for interface in namespace.interfaces:
                content: str = self.beginFile(namespace)
                content += self.interfaceText(enum, indent=1)
                content += self.endFile(namespace)
                result.append(dotnet_code(path, interface.name, content))

        return result

    def fileHeader(self) -> str:
        return self.configuration.fileHeader

    def defaultUsings(self) -> str:
        using_statements: List[str] = []

        for using in self.configuration.defaultUsings:
            using_statements.append(f"using {using};")

        return "\n".join(using_statements)

    def beginFile(self, namespace: namespace) -> str:
        buffer = io.StringIO()
        buffer.write(self.fileHeader())
        buffer.write("\n")
        buffer.write(self.defaultUsings())
        buffer.write("\n")
        buffer.write(f"namespace {namespace.name.getText()}\n")
        buffer.write("{\n")
        return buffer.getvalue()

    def endFile(self, namespace: namespace):
        buffer = io.StringIO()
        buffer.write("\n")
        buffer.write(f"}} // end of {namespace.name.getText()}\n")
        return buffer.getvalue()

    def enumText(self, enum: enum, indent: int = 1):
        buffer = io.StringIO()
        buffer.write("\n")
        buffer.write(f"{'\t'*indent}enum {enum.name}\n")
        buffer.write(f"{'\t'*indent}{{\n")
        for enum_element in enum.enum_elements:
            buffer.write(f"{'\t'*(indent+1)}{enum_element.value},\n")
        buffer.write(f"{'\t'*indent}}}\n")
        return buffer.getvalue()

    def interfaceText(self, interface: interface, indent: int = 1):
        buffer = io.StringIO()
        buffer.write("\n")
        buffer.write(f"{'\t'*indent}interface {interface.name}")
        buffer.write("{")
        for property in interface.properties:
            buffer.write(f"{self.propertyText(property, indent+1)},")
        for method in interface.methods:
            buffer.write(f"{self.methodText(method, indent+1)},")
        buffer.write(f"{'\t'*indent}}}\n")
        return buffer.getvalue()

    def propertyText(self, interface_property: interface_property, indent: int):
        buffer = io.StringIO()
        buffer.write(f"{'\t'*indent}public {self.typeText(type)} {interface_property.name} {{ get; ")
        if (interface_property.isReadonly == False):
            buffer.write(f"set; }}")
        return buffer.getvalue()

    def typeText(self, type: type):
        match type.kind:
            case type.Kind.Primitive:
                return self.typeTextPrimitive(type)
            case type.Kind.Reference:
                return self.typeTextReference(type)
            case type.Kind.List:
                return self.typeTextList(type)
            case type.Kind.Map:
                return self.typeTextMap(type)

    def typeTextPrimitive(self, type: primitive_type, indent: int):
        match type.primtiveKind:
            case primitive_type.PrimtiveKind.Integer:
                return "int"
            case primitive_type.PrimtiveKind.Number:
                return "decimal"
            case primitive_type.PrimtiveKind.Float:
                return "double"
            case primitive_type.PrimtiveKind.Date:
                return "System.DateOnly"
            case primitive_type.PrimtiveKind.Time:
                return "System.TimeOnly"
            case primitive_type.PrimtiveKind.DateTime:
                return "System.DateTime"
            case primitive_type.PrimtiveKind.String:
                return "string"
            case primitive_type.PrimtiveKind.Boolean:
                return "bool"
            case primitive_type.PrimtiveKind.Bytes:
                return "byte[]"

    def typeTextReference(self, type: reference_type, indent: int):
        return type.reference_name.getText()

    def typeTextList(self, type: list_type, indent: int):
        return f"System.Generic.List<{self.typeText(type.item_type)}>"

    def typeTextMap(self, type: map_type, indent: int):
        return f"System.Generic.Dictionary<{self.typeText(type.key_type)},{self.typeText(type.value_type)}>"


class utils:
    @staticmethod
    def create_folder(output_dir: str, folder_name: str):
        folder_path = os.path.join(output_dir, folder_name)
        os.makedirs(folder_path, exist_ok=True)

    @staticmethod
    def create_cs_file(output_dir: str, file_name: str, content: str):
        file_path = os.path.join(output_dir, file_name + ".cs")
        with open(file_path, "w") as file:
            file.write(content)


class dotnet_configuration:
    def __init__(self, configuration: Dict[str, str], output_dir: str):
        self.output_dir = output_dir

        self.__read_fileHeader(configuration)
        self.__read_defaultUsings(configuration)
        self.__read_createFolderStructure(configuration)

    def __read_fileHeader(self, configuration: Dict[str, str]):
        self.fileHeader: str = """
// <auto-generated>
//     This code was generated by unicontract
//     see more information: https://github.com/gyorgy-gulyas/UniContract
//
//     Changes to this file may cause incorrect behavior and will be lost if the code is regenerated.
// </auto-generated>
"""

        if "dotnet.file_header_lines" in configuration:
            value = configuration["dotnet.file_header_lines"]
            if (isinstance(value, list) and all(isinstance(item, str) for item in value)):
                self.fileHeader = "\n".join(value)

    def __read_defaultUsings(self, configuration: Dict[str, str]):
        self.defaultUsings: List[str] = ["System", "System.Threading.Tasks", "System.Collections.Generic"]
        if "dotnet.default_usings" in configuration:
            value = configuration["dotnet.default_usings"]
            if (isinstance(value, list) and all(isinstance(item, str) for item in value)):
                self.defaultUsings = value

    def __read_createFolderStructure(self, configuration: Dict[str, str]):
        self.createFolderStructure: bool = True
        if "dotnet.create_folder_structure" in configuration:
            self.createFolderStructure = bool(configuration["dotnet.create_folder_structure"])


class dotnet_code:
    def __init__(self, directory: str, name: str, content: str):
        self.fileName: str = name+".cs"
        self.fullPath: str = os.path.join(directory, self.fileName)
        self.content: str = content
