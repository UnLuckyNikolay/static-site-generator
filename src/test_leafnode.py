import unittest
from leafnode import *


class TestLeafNode(unittest.TestCase):
    def test_to_html(self):
        node1 = LeafNode("p", "Test case")
        self.assertEqual(node1.to_html(), "<p>Test case</p>")

    def test_to_html_with_props(self):
        node1 = LeafNode("h1", "You ain't gonna believe this new leak!", { "href":"https://www.youtube.com/watch?v=dQw4w9WgXcQ" })
        self.assertEqual(node1.to_html(), "<h1 href=\"https://www.youtube.com/watch?v=dQw4w9WgXcQ\">You ain't gonna believe this new leak!</h1>")

    def test_to_html_no_tag(self):
        node1 = LeafNode(None, "Just text")
        self.assertEqual(node1.to_html(), "Just text")


if __name__ == "__main__":
    unittest.main()