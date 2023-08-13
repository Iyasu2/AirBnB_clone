import unittest
from models.engine.file_storage import FileStorage
from models.base_model import BaseModel
import os


class TestFileStorage(unittest.TestCase):

    def setUp(self):
        """Set up test methods"""
        self.storage = FileStorage()
        self.model = BaseModel()

    def tearDown(self):
        """Tear down test methods"""
        if os.path.exists("file.json"):
            os.remove("file.json")

    def test_all(self):
        """Test all method"""
        self.assertEqual(dict, type(self.storage.all()))

    def test_new(self):
        """Test new method"""
        self.storage.new(self.model)
        key = "{}.{}".format(self.model.__class__.__name__, self.model.id)
        self.assertTrue(key in self.storage.all())

    def test_save(self):
        """Test save method"""
        self.storage.new(self.model)
        self.storage.save()
        self.assertTrue(os.path.exists("file.json"))

    def test_reload(self):
        """Test reload method"""
        self.storage.save()
        storage = FileStorage()
        storage.reload()
        self.assertEqual(len(storage.all()), len(self.storage.all()))


if __name__ == "__main__":
    unittest.main()
