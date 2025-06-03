import unittest
from textnode import *


class TestTextNode(unittest.TestCase):
    def test_eq(self):
        node = TextNode("Test", TextType.BOLD)
        node2 = TextNode("Test", TextType.BOLD, None)
        self.assertEqual(node, node2)

    def test_eq_false(self):
        node = TextNode("Test", TextType.BOLD)
        node2 = TextNode("Test", TextType.ITALIC)
        self.assertNotEqual(node, node2)

    def test_not_uq_url(self):
        node = TextNode("Test", TextType.LINK, "https://guthib.com")
        node2 = TextNode("Test", TextType.LINK, "https://github.com")
        self.assertNotEqual(node, node2)


if __name__ == "__main__":
    unittest.main()