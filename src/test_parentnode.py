import unittest
from parentnode import ParentNode
from leafnode import LeafNode


class TestParentNode(unittest.TestCase):
    def test_to_html_with_children(self):
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

    def test_to_html_with_grandchildren(self):
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



if __name__ == "__main__":
    unittest.main()