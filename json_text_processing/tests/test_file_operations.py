import unittest
import json
import os

class TestFileOperations(unittest.TestCase):

    def setUp(self):
        self.test_file = 'test_data.json'
        self.test_data = {
            "title": "Test Book",
            "author": "Test Author",
            "year": 2020,
            "genre": "Fiction"
        }

    def tearDown(self):
        if os.path.exists(self.test_file):
            os.remove(self.test_file)

    def test_write_and_read_file(self):
        with open(self.test_file, 'w') as file:
            json.dump(self.test_data, file)

        with open(self.test_file, 'r') as file:
            data = json.load(file)

        self.assertEqual(data, self.test_data)
        self.assertIsInstance(data['title'], str)
        self.assertIsInstance(data['author'], str)
        self.assertIsInstance(data['year'], int)
        self.assertIsInstance(data['genre'], str)

    def test_write_and_read_empty_file(self):
        with open(self.test_file, 'w') as file:
            json.dump({}, file)

        with open(self.test_file, 'r') as file:
            data = json.load(file)

        self.assertEqual(data, {})

    def test_read_nonexistent_file(self):
        with self.assertRaises(FileNotFoundError):
            with open('nonexistent_file.json', 'r') as file:
                json.load(file)

    def test_write_bad_data_into_file(self):
        with self.assertRaises(TypeError):
            with open(self.test_file, 'w') as file:
                json.dump(set([1, 2, 3]), file)

if __name__ == '__main__':
    unittest.main()