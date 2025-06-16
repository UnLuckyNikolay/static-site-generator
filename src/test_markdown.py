import unittest
from main import extract_title

class TestMarkdown(unittest.TestCase):
    def test__extract_title(self):
        markdown = """
# Title

text
"""
        title = extract_title(markdown)
        self.assertEqual(title, "Title")

    def test__extract_title_2(self):
        markdown = """
text

# Title

more text
"""
        title = extract_title(markdown)
        self.assertEqual(title, "Title")
        
    def test__extract_title__multiple_h1(self):
        markdown = """
# Title

# Another title?
"""
        title = extract_title(markdown)
        self.assertEqual(title, "Title")



if __name__ == "__main__":
    unittest.main()
    