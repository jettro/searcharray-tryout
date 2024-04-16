import unittest
from searcharray_tryout.util import ws_punc_tokenizer


class TestWsPuncTokenizer(unittest.TestCase):
    def test_tokenizes_text_without_punctuation(self):
        text = "hello world"
        expected = ["hello", "world"]
        self.assertEqual(expected, ws_punc_tokenizer(text))

    def test_tokenizes_text_with_punctuation(self):
        text = "hello, world!"
        expected = ["hello", "world"]
        self.assertEqual(expected, ws_punc_tokenizer(text))

    def test_tokenizes_text_with_multiple_spaces(self):
        text = "hello   world"
        expected = ["hello", "world"]
        self.assertEqual(expected, ws_punc_tokenizer(text))

    def test_tokenizes_empty_text(self):
        text = ""
        expected = []
        self.assertEqual(expected, ws_punc_tokenizer(text))

    def test_tokenizes_text_with_only_punctuation(self):
        text = "!!!"
        expected = [""]
        self.assertEqual(expected, ws_punc_tokenizer(text))

    def test_tokenizes_text_with_hyphen(self):
        text = "hello-world"
        expected = ["hello", "world"]
        self.assertEqual(expected, ws_punc_tokenizer(text))

    def test_tokenizes_text_with_multiple_hyphens(self):
        text = "hello-world-programming"
        expected = ["hello", "world", "programming"]
        self.assertEqual(expected, ws_punc_tokenizer(text))

    def test_tokenizes_text_with_hyphen_and_spaces(self):
        text = "hello - world"
        expected = ["hello", "-", "world"]
        self.assertEqual(expected, ws_punc_tokenizer(text))


if __name__ == '__main__':
    unittest.main()