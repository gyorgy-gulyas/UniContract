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

    def test_python_keywords_are_escaped(self):
        # A contract is free to name things 'from', 'class' or 'lambda' - every other target
        # language accepts them. In Python they are reserved, so emitting them verbatim produces a
        # module that does not even parse.
        results = self._emit("""
namespace N {
    interface ISearchIndex {
        property lambda: string
        readonly property pass: integer
        method Search( queryText: string, from: integer, size: integer ) => boolean
        method Raise( global: string )
    }
}""")
        c = self._content(results, "N.py")
        self.assertIn("def lambda_(self) -> str:", c)
        self.assertIn("@lambda_.setter", c)
        self.assertIn("def pass_(self) -> int:", c)
        self.assertNotIn("@pass_.setter", c)
        self.assertIn("def Search(self, queryText: str, from_: int, size: int) -> bool:", c)
        self.assertIn("def Raise(self, global_: str) -> None:", c)
        self._assert_runs(results)

    def test_non_keywords_are_left_alone(self):
        # Only real collisions are renamed; soft keywords are legal identifiers in Python and a
        # gratuitous rename would break the contract's own naming for no reason.
        results = self._emit("""
namespace N {
    interface I {
        property match: string
        property type: string
        method format( id: string )
    }
}""")
        c = self._content(results, "N.py")
        self.assertIn("def match(self) -> str:", c)
        self.assertIn("def type(self) -> str:", c)
        self.assertIn("def format(self, id: str) -> None:", c)
        self._assert_runs(results)

    def test_keyword_enum_member_keeps_its_wire_value(self):
        # The member name has to be escaped, but the value is what travels over the wire and must
        # stay exactly as the contract wrote it.
        results = self._emit("""
namespace N {
    interface I {
        enum Kind {
            None,
            Other
        }
    }
}""")
        c = self._content(results, "N.py")
        self.assertIn('None_ = "None"', c)
        self.assertIn('Other = "Other"', c)
        self._assert_runs(results)


if __name__ == "__main__":
    unittest.main()
