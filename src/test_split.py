import unittest
from functions_split import *

class TestSplitFunctions(unittest.TestCase):
    def test__markdown_to_blocks(self):
        input = """
This is **bolded** paragraph

This is another paragraph with _italic_ text and `code` here
This is the same paragraph on a new line

- This is a list
- with items
"""
        blocks = markdown_to_blocks(input)
        self.assertEqual(
            blocks,
            [
                "This is **bolded** paragraph",
                "This is another paragraph with _italic_ text and `code` here\nThis is the same paragraph on a new line",
                "- This is a list\n- with items",
            ],
        )

    def test__markdown_to_blocks__empty_blocks_and_whitespaces(self):
        input = """
- Start of a list
- Middle of a list
- End of a list

  

      






   

- Another List
"""
        blocks = markdown_to_blocks(input)
        self.assertEqual(
            blocks,
            [
                "- Start of a list\n- Middle of a list\n- End of a list",
                "- Another List",
            ],
        )

    def test__markdown_to_blocks__empty_blocks_and_whitespaces_2(self):
        input = """

 
 
 
"""
        blocks = markdown_to_blocks(input)
        self.assertEqual(
            blocks,
            [],
        )


    
    def test__split_nodes__text(self):
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

    def test__split_nodes__textnode(self):
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

    def test__split_nodes__list(self):
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

    def test__split_nodes__exception(self):
        with self.assertRaises(Exception):
            nodes = split_nodes(1)



    def test__split_nodes_by_type__bold(self):
        node = TextNode("**BIG** NEW CLUE FOUND!", TextType.TEXT)
        nodes = split_nodes_by_type(node, TextType.BOLD)
        self.assertEqual(nodes, [TextNode("BIG", TextType.BOLD), TextNode(" NEW CLUE FOUND!", TextType.TEXT)])
        
    def test__split_nodes_by_type__italic(self):
        node = TextNode("THE SLICK BIGMAN WAS SEEN _IN THE FOREST!_", TextType.TEXT)
        nodes = split_nodes_by_type(node, TextType.ITALIC)
        self.assertEqual(nodes, [TextNode("THE SLICK BIGMAN WAS SEEN ", TextType.TEXT), TextNode("IN THE FOREST!", TextType.ITALIC)])
        
    def test__split_nodes_by_type__code(self):
        node = TextNode("`CHECK OUT NEW STORY BELOW`", TextType.TEXT)
        nodes = split_nodes_by_type(node, TextType.CODE)
        self.assertEqual(nodes, [TextNode("CHECK OUT NEW STORY BELOW", TextType.CODE)])
        
    def test__split_nodes_by_type__image(self):
        node = TextNode("LOOK AT THIS PHOTOGRAPH: ![bigman](C:/secret_files/bigman_018.jfeck)", TextType.TEXT)
        nodes = split_nodes_by_type(node, TextType.IMAGE)
        self.assertEqual(nodes, [TextNode("LOOK AT THIS PHOTOGRAPH: ", TextType.TEXT), TextNode("bigman", TextType.IMAGE, "C:/secret_files/bigman_018.jfeck")])
        
    def test__split_nodes_by_type__link(self):
        node = TextNode("READ FULL STORY HERE: [bigman blog](htppsp://acebook.moc/followers_of_the_man)", TextType.TEXT)
        nodes = split_nodes_by_type(node, TextType.LINK)
        self.assertEqual(nodes, [TextNode("READ FULL STORY HERE: ", TextType.TEXT), TextNode("bigman blog", TextType.LINK, "htppsp://acebook.moc/followers_of_the_man")])

    def test__split_nodes_by_type__bold_base__checks_a_mistake(self): # Switches RISE to Italic for now
        node = TextNode("SOON WE WILL _RISE_", TextType.BOLD)
        nodes = split_nodes_by_type(node, TextType.ITALIC)
        self.assertEqual(nodes, [TextNode("SOON WE WILL ", TextType.BOLD), TextNode("RISE", TextType.ITALIC)])

    def test__split_nodes_by_type__two_images(self):
        node = TextNode("NEW SIGHTINGS! ONE: ![bigman_2](C:/secret_files/bigman_039.jfeck), TWO: ![bigman_3](C:/secret_files/bigman_040.jfeck)", TextType.TEXT)
        nodes = split_nodes_by_type(node, TextType.IMAGE)
        self.assertEqual(nodes, [
            TextNode("NEW SIGHTINGS! ONE: ", TextType.TEXT),
            TextNode("bigman_2", TextType.IMAGE, "C:/secret_files/bigman_039.jfeck"),
            TextNode(", TWO: ", TextType.TEXT),
            TextNode("bigman_3", TextType.IMAGE, "C:/secret_files/bigman_040.jfeck")
        ])



if __name__ == "__main__":
    unittest.main()