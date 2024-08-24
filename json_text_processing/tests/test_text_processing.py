import unittest

class TextProcessor:
    def clean_text(self, text):
        cleaned_text = ''.join([char.lower() for char in text if char.isalpha() or char.isspace()])
        return cleaned_text.strip()

    def remove_stop_words(self, text, stop_words):
        words = text.split()
        filtered_text = ' '.join([word for word in words if word not in stop_words])
        return filtered_text

class TestTextProcessing(unittest.TestCase):

    def setUp(self):
        self.processor = TextProcessor()

    def test_clean_text(self):
        result = self.processor.clean_text("Hello, World!")
        self.assertEqual(result, "hello world")

        result = self.processor.clean_text("123 ABC!!!")
        self.assertEqual(result, "abc")

        result = self.processor.clean_text("")
        self.assertEqual(result, "")

    def test_remove_stop_words(self):
        result = self.processor.remove_stop_words("this is a test", ['this', 'is'])
        self.assertEqual(result, "a test")

        result = self.processor.remove_stop_words("hello world", [])
        self.assertEqual(result, "hello world")

        result = self.processor.remove_stop_words("no stop words here", ['this', 'is', 'not', 'here'])
        self.assertEqual(result, "no stop words")

if __name__ == '__main__':
    unittest.main()