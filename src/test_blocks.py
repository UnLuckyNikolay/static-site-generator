import unittest
from functions_blocks import *

class TestBlockFunctions(unittest.TestCase):
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