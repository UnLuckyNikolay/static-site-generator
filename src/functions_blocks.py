import re

from textnode import TextNode, TextType
from enum import Enum

class BlockType(Enum):
    PARAGRAPH = "paragraph"
    HEADING = "heading"
    CODE = "code"
    QUOTE = "quote"
    UNORDERED_LIST = "unordered_list"
    ORDERED_LIST = "ordered_list"



def markdown_to_blocks(md_text):
    blocks = md_text.split("\n\n")

    blocks = list(map(lambda x: x.strip(), blocks))
    blocks = list(filter(lambda x: x != "", blocks))

    return blocks



def block_to_block_type(block):
    # Heading
    check_heading = block.split(" ", maxsplit=1)[0]
    pattern_heading = re.compile(r"(?<!.)(#{1,6})(?!.)")
    split_block = block.split("\n")

    if pattern_heading.match(check_heading):
        return BlockType.HEADING
    
    elif block[:3] == "```" and block[-3:] == "```":
        return BlockType.CODE
    
    elif check_start_of_lines(split_block, ">"):
        return BlockType.QUOTE
    
    elif check_start_of_lines(split_block, "- "):
        return BlockType.UNORDERED_LIST
    
    elif check_ordered_list(split_block):
        return BlockType.ORDERED_LIST

    else:
        return BlockType.PARAGRAPH
    
def check_start_of_lines(split_block, start):
    for line in split_block:
        if line[:len(start)] != start:
            return False
    return True


def check_ordered_list(split_block):
    i = 1
    for line in split_block:
        if line[:2] != f"{i}.":
            return False
        i+=1
    return True
