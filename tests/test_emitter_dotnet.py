import unittest
from pathlib import Path
from tests.dotnet_code_helper import *
from unicontract.emitters.DotnetEmmiter import *


class TestEmitterDotnetDefault(unittest.TestCase):

    def setUp(self):
        dotnet_code_helper.init_roslyn()

    def test_empty_ok(self):
        engine = Engine()
        session = Session(Source.CreateFromText(""""""))
        root = engine.Build(session)
        self.assertFalse(session.HasAnyError())

        emitter = DotnetEmmiter()
        result = emitter.Emit(session)
        self.assertEqual(len(result), 0)

    def test_empty_namespace_ok(self):
        engine = Engine()
        session = Session(Source.CreateFromText("""
namespace SomeNamespace{
}"""))
        root = engine.Build(session)
        self.assertFalse(session.HasAnyError())

        emitter = DotnetEmmiter()
        result = emitter.Emit(session)
        self.assertEqual(len(result), 0)

    def test_create_folder_structure_ok(self):
        engine = Engine()
        session = Session(Source.CreateFromText("""
namespace SomeNamespace.SubNameSpace{
    enum SomeEnum{
        Value1,
        Value2
    }
}"""))
        root = engine.Build(session)
        self.assertFalse(session.HasAnyError())

        emitter = DotnetEmmiter(configuration={"dotnet.create_folder_structure": True})
        result = emitter.Emit(session)
        self.assertEqual(len(result), 1)
        self.assertEqual(Path(result[0].fullPath), Path("./SomeNamespace/SubNameSpace/SomeEnum.cs"))

        emitter = DotnetEmmiter(configuration={"dotnet.create_folder_structure": False})
        result = emitter.Emit(session)
        self.assertEqual(len(result), 1)
        self.assertEqual(Path(result[0].fullPath), Path("./SomeEnum.cs"))

    def test_can_build_ok(self):
        engine = Engine()
        session = Session(Source.CreateFromText("""
namespace SomeNamespace{
    enum SomeEnum{
        Value1,
        Value2
    }
}"""))
        root = engine.Build(session)
        self.assertFalse(session.HasAnyError())

        emitter = DotnetEmmiter()
        result = emitter.Emit(session)
        self.assertEqual(len(result), 1)

        compiled, errors, assembly = dotnet_code_helper.compile_debug(result, dotnet_code_helper.assembly_name())
        self.assertTrue(compiled)

if __name__ == "__main__":
    unittest.main()
