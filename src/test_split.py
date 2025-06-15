import unittest
from functions_split import *

class TestSplitFunctions(unittest.TestCase):
    def test_bold(self):
        node = TextNode("**BIG** NEW CLUE FOUND!", TextType.TEXT)
        nodes = split_nodes_by_type(node, TextType.BOLD)
        self.assertEqual(nodes, [TextNode("BIG", TextType.BOLD), TextNode(" NEW CLUE FOUND!", TextType.TEXT)])
        
    def test_italic(self):
        node = TextNode("THE SLICK BIGMAN WAS SEEN _IN THE FOREST!_", TextType.TEXT)
        nodes = split_nodes_by_type(node, TextType.ITALIC)
        self.assertEqual(nodes, [TextNode("THE SLICK BIGMAN WAS SEEN ", TextType.TEXT), TextNode("IN THE FOREST!", TextType.ITALIC)])
        
    def test_code(self):
        node = TextNode("`CHECK OUT NEW STORY BELOW`", TextType.TEXT)
        nodes = split_nodes_by_type(node, TextType.CODE)
        self.assertEqual(nodes, [TextNode("CHECK OUT NEW STORY BELOW", TextType.CODE)])
        
    def test_image(self):
        node = TextNode("LOOK AT THIS PHOTOGRAPH: ![bigman](C:/secret_files/bigman_018.jfeck)", TextType.TEXT)
        nodes = split_nodes_by_type(node, TextType.IMAGE)
        self.assertEqual(nodes, [TextNode("LOOK AT THIS PHOTOGRAPH: ", TextType.TEXT), TextNode("bigman", TextType.IMAGE, "C:/secret_files/bigman_018.jfeck")])
        
    def test_link(self):
        node = TextNode("READ FULL STORY HERE: [bigman blog](htppsp://acebook.moc/followers_of_the_man)", TextType.TEXT)
        nodes = split_nodes_by_type(node, TextType.LINK)
        self.assertEqual(nodes, [TextNode("READ FULL STORY HERE: ", TextType.TEXT), TextNode("bigman blog", TextType.LINK, "htppsp://acebook.moc/followers_of_the_man")])

    def test_bold_base___checks_a_mistake(self): # Switches RISE to Italic for now
        node = TextNode("SOON WE WILL _RISE_", TextType.BOLD)
        nodes = split_nodes_by_type(node, TextType.ITALIC)
        self.assertEqual(nodes, [TextNode("SOON WE WILL ", TextType.BOLD), TextNode("RISE", TextType.ITALIC)])

    def test_two_images(self):
        node = TextNode("NEW SIGHTINGS! ONE: ![bigman_2](C:/secret_files/bigman_039.jfeck), TWO: ![bigman_3](C:/secret_files/bigman_040.jfeck)", TextType.TEXT)
        nodes = split_nodes_by_type(node, TextType.IMAGE)
        self.assertEqual(nodes, [
            TextNode("NEW SIGHTINGS! ONE: ", TextType.TEXT),
            TextNode("bigman_2", TextType.IMAGE, "C:/secret_files/bigman_039.jfeck"),
            TextNode(", TWO: ", TextType.TEXT),
            TextNode("bigman_3", TextType.IMAGE, "C:/secret_files/bigman_040.jfeck")
        ])


    def test_all_split_text(self):
        input = "This is **text** with an _italic_ word and a `code block` and an ![obi wan image](https://i.imgur.com/fJRm4Vk.jpeg) and a [link](https://boot.dev)"
        nodes = split_nodes(input)
        self.assertEqual(nodes, [
            TextNode("This is ", TextType.TEXT),
            TextNode("text", TextType.BOLD),
            TextNode(" with an ", TextType.TEXT),
            TextNode("italic", TextType.ITALIC),
            TextNode(" word and a ", TextType.TEXT),
            TextNode("code block", TextType.CODE),
            TextNode(" and an ", TextType.TEXT),
            TextNode("obi wan image", TextType.IMAGE, "https://i.imgur.com/fJRm4Vk.jpeg"),
            TextNode(" and a ", TextType.TEXT),
            TextNode("link", TextType.LINK, "https://boot.dev"),
        ])

    def test_all_split_textnode(self):
        input = TextNode("This is **text** with an _italic_ word and a `code block` and an ![obi wan image](https://i.imgur.com/fJRm4Vk.jpeg) and a [link](https://boot.dev)", TextType.TEXT)
        nodes = split_nodes(input)
        self.assertEqual(nodes, [
            TextNode("This is ", TextType.TEXT),
            TextNode("text", TextType.BOLD),
            TextNode(" with an ", TextType.TEXT),
            TextNode("italic", TextType.ITALIC),
            TextNode(" word and a ", TextType.TEXT),
            TextNode("code block", TextType.CODE),
            TextNode(" and an ", TextType.TEXT),
            TextNode("obi wan image", TextType.IMAGE, "https://i.imgur.com/fJRm4Vk.jpeg"),
            TextNode(" and a ", TextType.TEXT),
            TextNode("link", TextType.LINK, "https://boot.dev"),
        ])

    def test_all_split_list(self):
        input = [TextNode("This is **text** with an _italic_ word and a `code block` and an ![obi wan image](https://i.imgur.com/fJRm4Vk.jpeg) and a [link](https://boot.dev)", TextType.TEXT)]
        nodes = split_nodes(input)
        self.assertEqual(nodes, [
            TextNode("This is ", TextType.TEXT),
            TextNode("text", TextType.BOLD),
            TextNode(" with an ", TextType.TEXT),
            TextNode("italic", TextType.ITALIC),
            TextNode(" word and a ", TextType.TEXT),
            TextNode("code block", TextType.CODE),
            TextNode(" and an ", TextType.TEXT),
            TextNode("obi wan image", TextType.IMAGE, "https://i.imgur.com/fJRm4Vk.jpeg"),
            TextNode(" and a ", TextType.TEXT),
            TextNode("link", TextType.LINK, "https://boot.dev"),
        ])

    def test_all_split_exception(self):
        with self.assertRaises(Exception):
            nodes = split_nodes(1)