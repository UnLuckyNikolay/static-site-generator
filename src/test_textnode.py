import unittest
from textnode import *
from functions_blocks import text_node_to_html_node


class TestTextNode(unittest.TestCase):
    def test__textnode__eq(self):
        node = TextNode("Test", TextType.BOLD)
        node2 = TextNode("Test", TextType.BOLD, None)
        self.assertEqual(node, node2)

    def test__textnode__not_eq(self):
        node = TextNode("Test", TextType.BOLD)
        node2 = TextNode("Test", TextType.ITALIC)
        self.assertNotEqual(node, node2)

    def test__textnode__not_eq_url(self):
        node = TextNode("Test", TextType.LINK, "https://guthib.com")
        node2 = TextNode("Test", TextType.LINK, "https://github.com")
        self.assertNotEqual(node, node2)

    def test__textnode__to_html(self):
        node = TextNode("Heyo", TextType.TEXT)
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag, None)
        self.assertEqual(html_node.to_html(), "Heyo")

    def test__textnode__to_html_bold(self):
        node = TextNode("BIG", TextType.BOLD)
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag, "b")
        self.assertEqual(html_node.to_html(), "<b>BIG</b>")


if __name__ == "__main__":
    unittest.main()