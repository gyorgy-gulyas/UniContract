import unittest
from unicontract.Engine import *
from unicontract.emitters.PythonEmitter import *
from tests import python_code_helper


class TestEmitterPython(unittest.TestCase):

    def _emit(self, text):
        engine = Engine()
        session = Session(Source.CreateFromText(text))
        engine.Build(session)
        self.assertFalse(session.HasAnyError(), "contract had errors")
        return PythonEmitter().Emit(session)

    def _content(self, results, filename):
        return next(c.content for c in results if c.fileName == filename)

    def _assert_runs(self, results):
        ok, error = python_code_helper.check_python(results)
        self.assertTrue(ok, f"generated Python did not run:\n{error}")

    def test_empty_ok(self):
        self.assertEqual(len(self._emit("")), 0)

    def test_module_per_namespace(self):
        results = self._emit("""
namespace N {
    interface I {
    }
}""")
        self.assertEqual(len(results), 1)
        self.assertEqual(results[0].fileName, "N.py")

    def test_property_becomes_abstract_getter_and_setter(self):
        results = self._emit("""
namespace N {
    interface IEntity {
        property id: string
        readonly property createdAt: dateTime
    }
}""")
        c = self._content(results, "N.py")
        self.assertIn("class IEntity(ABC):", c)
        self.assertIn("@property", c)
        self.assertIn("@abstractmethod", c)
        self.assertIn("def id(self) -> str:", c)
        self.assertIn("@id.setter", c)
        self.assertIn("def id(self, value: str) -> None:", c)
        self.assertIn("def createdAt(self) -> datetime:", c)   # dateTime -> datetime
        self.assertNotIn("@createdAt.setter", c)               # readonly -> getter only
        self._assert_runs(results)

    def test_generics_bound_and_async(self):
        results = self._emit("""
namespace N {
    interface IEntity {
    }
    interface ICollection<T constraint IEntity> {
        async method Insert( entity: T ) => boolean
        async method Count()
    }
}""")
        c = self._content(results, "N.py")
        self.assertIn('T = TypeVar("T", bound="IEntity")', c)
        self.assertIn("class ICollection(ABC, Generic[T]):", c)
        self.assertIn("async def Insert(self, entity: T) -> bool:", c)
        self.assertIn("async def Count(self) -> None:", c)
        self._assert_runs(results)

    def test_type_mapping(self):
        results = self._emit("""
namespace N {
    interface ITypes {
        property i: integer
        property n: number
        property f: float
        property raw: bytes
        property items: list[string]
        property lookup: map[string, integer]
    }
}""")
        c = self._content(results, "N.py")
        self.assertIn("def i(self) -> int:", c)
        self.assertIn("def n(self) -> Decimal:", c)
        self.assertIn("def f(self) -> float:", c)
        self.assertIn("def raw(self) -> bytes:", c)
        self.assertIn("def items(self) -> List[str]:", c)
        self.assertIn("def lookup(self) -> Dict[str, int]:", c)
        self._assert_runs(results)

    def test_enum_ok(self):
        results = self._emit("""
namespace N {
    interface IStore {
        enum Kind {
            A,
            B
        }
    }
}""")
        c = self._content(results, "N.py")
        self.assertIn("class Kind(Enum):", c)
        self.assertIn('A = "A"', c)
        self.assertIn('B = "B"', c)
        self._assert_runs(results)


if __name__ == "__main__":
    unittest.main()
