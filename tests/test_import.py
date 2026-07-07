import unittest
import os
from unicontract.Engine import *


class TestImportMerge(unittest.TestCase):
    """UNI-17: the import/merge path was untested."""

    def _sample(self, *parts):
        return os.path.normpath(os.path.join(os.path.dirname(__file__), "..", "sample", *parts))

    def test_datastore_imports_resolve_and_merge(self):
        # IDataStore imports IConnection, ICollection and IEntity from the same folder.
        engine = Engine()
        session = Session(Source.CreateFromFile(self._sample("datastore", "IDataStore.contract")))
        engine.Build(session)

        self.assertFalse(session.HasAnyError())
        self.assertGreaterEqual(len(session.main.imports), 3)
        for imp in session.main.imports:
            self.assertIsNotNone(imp.contract, f"import '{imp.name}' did not resolve to a contract")

        loaded = " ".join(session.all.keys())
        for name in ("IConnection", "ICollection", "IEntity"):
            self.assertIn(name, loaded)

    def test_missing_import_reports_error(self):
        engine = Engine()
        session = Session(Source.CreateFromText("import DoesNotExist\nnamespace N {\n}\n"))
        engine.Build(session)
        self.assertTrue(session.HasAnyError())


if __name__ == "__main__":
    unittest.main()
