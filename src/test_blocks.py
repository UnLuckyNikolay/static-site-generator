import unittest
from functions_blocks import *

class TestBlockFunctions(unittest.TestCase):
    def test__markdown_to_html_node__paragraphs(self):
        md = """
This is **bolded** paragraph
text in a p
tag here

This is another paragraph with _italic_ text and `code` here

"""

        node = markdown_to_html_node(md)
        html = node.to_html()
        self.assertEqual(
            html,
            "<div><p>This is <b>bolded</b> paragraph text in a p tag here</p><p>This is another paragraph with <i>italic</i> text and <code>code</code> here</p></div>",
        )

    def test__markdown_to_html_node__code(self):
        md = """
```
This is text that _should_ remain
the **same** even with inline stuff
```
"""

        node = markdown_to_html_node(md)
        html = node.to_html()
        self.assertEqual(
            html,
            "<div><pre><code>This is text that _should_ remain\nthe **same** even with inline stuff\n</code></pre></div>",
        )

    def test__markdown_to_html_node__ordered_list(self):
        md = """
1. We're no strangers to love
2. You know the rules and so do I
3. A full commitment's what I'm thinkin' of
4. You wouldn't get this from any other guy
"""

        node = markdown_to_html_node(md)
        html = node.to_html()
        self.assertEqual(
            html,
            "<div><ol><li>We're no strangers to love</li><li>You know the rules and so do I</li><li>A full commitment's what I'm thinkin' of</li><li>You wouldn't get this from any other guy</li></ol></div>",
        )

    def test__markdown_to_html_node__quote(self):
        md = """
>I just wanna tell you how I'm feeling
>Gotta make you understand
"""

        node = markdown_to_html_node(md)
        html = node.to_html()
        self.assertEqual(
            html,
            "<div><blockquote>I just wanna tell you how I'm feeling Gotta make you understand</blockquote></div>",
        )

    def test__markdown_to_html_node__unordered_list(self):
        md = """
- Never gonna give you up, never gonna let you down
- Never gonna run around and desert you
- Never gonna make you cry, never gonna say goodbye
- Never gonna tell a lie and hurt you
"""

        node = markdown_to_html_node(md)
        html = node.to_html()
        self.assertEqual(
            html,
            "<div><ul><li>Never gonna give you up, never gonna let you down</li><li>Never gonna run around and desert you</li><li>Never gonna make you cry, never gonna say goodbye</li><li>Never gonna tell a lie and hurt you</li></ul></div>",
        )

    def test__markdown_to_html_node__headings(self):
        md = """
# You can have the biggest heading

## And a bit smaller one

### And even another smaller one

#### Then we have some medium ones

##### Some S sizes

###### Baby's first headings

####### This one is still growing to become a heading
"""

        node = markdown_to_html_node(md)
        html = node.to_html()
        self.assertEqual(
            html,
            "<div><h1>You can have the biggest heading</h1><h2>And a bit smaller one</h2><h3>And even another smaller one</h3><h4>Then we have some medium ones</h4><h5>Some S sizes</h5><h6>Baby's first headings</h6><p>####### This one is still growing to become a heading</p></div>",
        )



    def test__block_to_block_type__heading(self):
        input = "#### Imma head out"
        block = block_to_block_type(input)
        self.assertEqual(BlockType.HEADING, block)

    def test__block_to_block_type__heading_wrong(self):
        input = "######## Will be back later"
        block = block_to_block_type(input)
        self.assertEqual(BlockType.PARAGRAPH, block)


    def test__block_to_block_type__code(self):
        input = "```print(Hello World)```"
        block = block_to_block_type(input)
        self.assertEqual(BlockType.CODE, block)

    def test__block_to_block_type__code_wrong(self):
        input = "``game.start()``"
        block = block_to_block_type(input)
        self.assertEqual(BlockType.PARAGRAPH, block)


    def test__block_to_block_type__quote(self):
        input = (
"""> How fine you look when dressed in rage. 
>Cheshire""")
        block = block_to_block_type(input)
        self.assertEqual(BlockType.QUOTE, block)

    def test__block_to_block_type__quote_wrong(self):
        input = (
"""> ...only level 62...
Elon Mask""")
        block = block_to_block_type(input)
        self.assertEqual(BlockType.PARAGRAPH, block)


    def test__block_to_block_type__unordered_list(self):
        input = (
"""- What will we do with a drunken sailor?
- What will we do with a drunken sailor?
- What will we do with a drunken sailor?
- Early in the morning!""")
        block = block_to_block_type(input)
        self.assertEqual(BlockType.UNORDERED_LIST, block)

    def test__block_to_block_type__unordered_list_wrong(self):
        input = (
"""Stuff to buy:
- Milk
- Coffee
- Matches
- Gasoline""")
        block = block_to_block_type(input)
        self.assertEqual(BlockType.PARAGRAPH, block)


    def test__block_to_block_type__ordered_list(self):
        input = (
"""1. Steal the Declaration of Independence
2. ?????
3. Profit""")
        block = block_to_block_type(input)
        self.assertEqual(BlockType.ORDERED_LIST, block)

    def test__block_to_block_type__ordered_list_wrong(self):
        input = (
"""1. Wake up
2. Burn the horde
3. Clean the teeth
4. Burn the horde
5. Breakfast
6. Horde
7. Horde
10. Horde
21. Horde""")
        block = block_to_block_type(input)
        self.assertEqual(BlockType.PARAGRAPH, block)


    def test__block_to_block_type__paragraph(self):
        input = "Just plain text"
        block = block_to_block_type(input)
        self.assertEqual(BlockType.PARAGRAPH, block)



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


    
if __name__ == "__main__":
    unittest.main()