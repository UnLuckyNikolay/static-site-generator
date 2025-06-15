import unittest
from htmlnode import *


class TestHTMLNode(unittest.TestCase):
    def test__htmlnode__eq(self):
        node1 = HTMLNode()
        node2 = HTMLNode()
        self.assertEqual(node1, node2)

    def test__htmlnode__eq2(self):
        node1 = HTMLNode("p", "Test node", [], {"test key":"test value"})
        node2 = HTMLNode("p", "Test node", [], {"test key":"test value"})
        self.assertEqual(node1, node2)

    def test__htmlnode__repr(self):
        node1 = HTMLNode("p", "Test node", None, {"test key":"test value"})
        self.assertEqual("HTMLNode(p, Test node, None, {'test key': 'test value'})", repr(node1))

    def test__htmlnode__props_to_html(self):
        node1 = HTMLNode("p", "Test node", None, {"test key":"test value", "key2":"value2"})
        self.assertEqual(" test key=\"test value\" key2=\"value2\"", node1.props_to_html())



class TestParentNode(unittest.TestCase):
    def test__parentnode__with_children(self):
        node1 = ParentNode(
            "p",
            [
                LeafNode("b", "One, two, three, "),
                LeafNode(None, "four, five, six, "),
                LeafNode("i", "seven, eight, nine.")
            ],
            None
        )
        self.assertEqual(node1.to_html(), "<p><b>One, two, three, </b>four, five, six, <i>seven, eight, nine.</i></p>")

    def test__parentnode__with_grandchildren(self):
        child1 = ParentNode(
            "p",
            [
                LeafNode("b", "One, "),
                LeafNode(None, "two, "),
                LeafNode("i", "three, ")
            ],
            None
        )
        child2 = ParentNode(
            "p",
            [
                LeafNode("b", "four, "),
                LeafNode(None, "five, "),
                LeafNode("i", "six.")
            ],
            None
        )
        node1 = ParentNode(
            "outer",
            [child1, child2],
            None
        )
        self.assertEqual(node1.to_html(), "<outer><p><b>One, </b>two, <i>three, </i></p><p><b>four, </b>five, <i>six.</i></p></outer>")



class TestLeafNode(unittest.TestCase):
    def test__leafnode(self):
        node1 = LeafNode("p", "Test case")
        self.assertEqual(node1.to_html(), "<p>Test case</p>")

    def test__leafnode__with_props(self):
        node1 = LeafNode("h1", "You ain't gonna believe this new leak!", { "href":"https://www.youtube.com/watch?v=dQw4w9WgXcQ" })
        self.assertEqual(node1.to_html(), "<h1 href=\"https://www.youtube.com/watch?v=dQw4w9WgXcQ\">You ain't gonna believe this new leak!</h1>")

    def test__leafnode__no_tag(self):
        node1 = LeafNode(None, "Just text")
        self.assertEqual(node1.to_html(), "Just text")



if __name__ == "__main__":
    unittest.main()