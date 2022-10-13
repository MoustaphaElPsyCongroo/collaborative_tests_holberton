#!/usr/bin/python3
"Unit tests for FileStorage class"
import unittest
from models.engine.file_storage import FileStorage


class TestFileStorage(unittest.TestCase):
    "Unit tests suite for FileStorage class"

    def test_instanciates(self):
        "Tests that FileStorage correctly instanciates"
        storage = FileStorage()
        self.assertIsInstance(storage, FileStorage)

    def test_file_path(self):
        """Test __file path is exited"""
        path = FileStorage._FileStorage__file_path
        self.assertEqual(str, type(path))


if __name__ == "__main__":
    unittest.main()
