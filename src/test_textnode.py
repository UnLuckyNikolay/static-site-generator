import unittest
from textnode import *
from main import text_node_to_html_node, split_nodes_delimiter


class TestSplitNodes(unittest.TestCase):
    def test_missing_delimiter(self):
        node = TextNode("Another one **bites the dust", TextType.TEXT)
        self.assertRaises(Exception, split_nodes_delimiter, [node], "**")

    def test_invalid(self):
        node = TextNode("Let's `finally` **test** _this_ shit", TextType.TEXT)
        self.assertRaises(Exception, split_nodes_delimiter, [node], "whoops")

    def test_code(self):
        node = TextNode("Let's `finally` **test** _this_ shit", TextType.TEXT)
        nodes = split_nodes_delimiter([node], "`")
        self.assertEqual(TextNode("finally", TextType.CODE), nodes[1])

    def test_italic(self):
        node = TextNode("Let's `finally` **test** _this_ shit", TextType.TEXT)
        nodes = split_nodes_delimiter([node], "**")
        self.assertEqual(TextNode("test", TextType.BOLD), nodes[1])

    def test_bold(self):
        node = TextNode("Let's `finally` **test** _this_ shit", TextType.TEXT)
        nodes = split_nodes_delimiter([node], "_")
        self.assertEqual(TextNode("this", TextType.ITALIC), nodes[1])

    # Checks if enpty nodes are removed
    def test_bold_at_the_start(self):
        node = TextNode("**WE** ROCK!", TextType.TEXT)
        nodes = split_nodes_delimiter([node], "**")
        self.assertEqual(TextNode("WE", TextType.BOLD), nodes[0])

    def test_plain_text(self):
        node = TextNode("Nice weather today", TextType.TEXT)
        nodes = split_nodes_delimiter([node], "**")
        self.assertEqual(node, nodes[0])

    def test_not_plain_text(self):
        node = TextNode("_Storm_ incoming!", TextType.BOLD)
        nodes = split_nodes_delimiter([node], "_")
        self.assertEqual(node, nodes[0])


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

    def test_text_to_html(self):
        node = TextNode("Heyo", TextType.TEXT)
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag, None)
        self.assertEqual(html_node.to_html(), "Heyo")

    def test_text_to_html_bold(self):
        node = TextNode("BIG", TextType.BOLD)
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag, "b")
        self.assertEqual(html_node.to_html(), "<b>BIG</b>")


if __name__ == "__main__":
    unittest.main()