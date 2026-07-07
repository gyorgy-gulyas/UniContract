import unittest
from unicontract.Engine import *
from unicontract.emitters.JavaEmitter import *
from tests import java_code_helper


class TestEmitterJava(unittest.TestCase):

    def _emit(self, text):
        engine = Engine()
        session = Session(Source.CreateFromText(text))
        engine.Build(session)
        self.assertFalse(session.HasAnyError(), "contract had errors")
        return JavaEmitter().Emit(session)

    def _content(self, results, filename):
        return next(c.content for c in results if c.fileName == filename)

    def _assert_compiles(self, results):
        ok, output = java_code_helper.compile_java(results)
        if ok is None:
            self.skipTest("javac not available")
        self.assertTrue(ok, f"javac failed:\n{output}")

    def test_empty_ok(self):
        self.assertEqual(len(self._emit("")), 0)

    def test_property_becomes_getter_and_setter(self):
        results = self._emit("""
namespace N {
    interface IEntity {
        property id: string
        readonly property createdAt: dateTime
    }
}""")
        c = self._content(results, "IEntity.java")
        self.assertIn("package N;", c)
        self.assertIn("public interface IEntity {", c)
        self.assertIn("String getId();", c)
        self.assertIn("void setId(String value);", c)
        self.assertIn("LocalDateTime getCreatedAt();", c)   # dateTime -> LocalDateTime
        self.assertNotIn("setCreatedAt", c)                 # readonly -> getter only
        self._assert_compiles(results)

    def test_generics_extends_and_async(self):
        results = self._emit("""
namespace N {
    interface IEntity {
    }
    interface ICollection<T constraint IEntity> {
        async method Insert( entity: T ) => boolean
        async method Count()
    }
}""")
        c = self._content(results, "ICollection.java")
        self.assertIn("public interface ICollection<T extends IEntity>", c)  # constraint inline
        self.assertIn("CompletableFuture<Boolean> Insert(T entity);", c)     # async + boxed bool
        self.assertIn("CompletableFuture<Void> Count();", c)                 # async, no return
        self._assert_compiles(results)

    def test_generic_method_type_params_before_return_type(self):
        results = self._emit("""
namespace N {
    interface IBase {
    }
    interface IStore {
        method Resolve<T constraint IBase>( name: string ) => T
    }
}""")
        c = self._content(results, "IStore.java")
        self.assertIn("<T extends IBase> T Resolve(String name);", c)
        self._assert_compiles(results)

    def test_primitive_and_collection_type_mapping(self):
        results = self._emit("""
namespace N {
    interface ITypes {
        property i: integer
        property f: float
        property n: number
        property b: boolean
        property raw: bytes
        property items: list[string]
        property lookup: map[string, integer]
    }
}""")
        c = self._content(results, "ITypes.java")
        self.assertIn("int getI();", c)
        self.assertIn("double getF();", c)
        self.assertIn("BigDecimal getN();", c)
        self.assertIn("boolean getB();", c)
        self.assertIn("byte[] getRaw();", c)
        self.assertIn("List<String> getItems();", c)
        self.assertIn("Map<String, Integer> getLookup();", c)   # primitive boxed inside a generic
        self._assert_compiles(results)

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
        c = self._content(results, "IStore.java")
        self.assertIn("public enum Kind {", c)
        self.assertIn("A,", c)
        self.assertIn("B,", c)
        self._assert_compiles(results)


if __name__ == "__main__":
    unittest.main()
