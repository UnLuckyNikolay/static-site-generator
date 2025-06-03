import unittest
from htmlnode import *


class TestHTMLNode(unittest.TestCase):
    def test_eq(self):
        node1 = HTMLNode()
        node2 = HTMLNode()
        self.assertEqual(node1, node2)

    def test_eq2(self):
        node1 = HTMLNode("p", "Test node", [], {"test key":"test value"})
        node2 = HTMLNode("p", "Test node", [], {"test key":"test value"})
        self.assertEqual(node1, node2)

    def test_repr(self):
        node1 = HTMLNode("p", "Test node", None, {"test key":"test value"})
        self.assertEqual("HTMLNode(p, Test node, None, {'test key': 'test value'})", repr(node1))

    def test_props_to_html(self):
        node1 = HTMLNode("p", "Test node", None, {"test key":"test value", "key2":"value2"})
        self.assertEqual(" test key=\"test value\" key2=\"value2\"", node1.props_to_html())

if __name__ == "__main__":
    unittest.main()