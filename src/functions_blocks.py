import re

from textnode import TextNode, TextType
from enum import Enum
from htmlnode import ParentNode, LeafNode
from functions_split import split_nodes

class BlockType(Enum):
    PARAGRAPH = "paragraph"
    HEADING = "heading"
    CODE = "code"
    QUOTE = "quote"
    UNORDERED_LIST = "unordered list"
    ORDERED_LIST = "ordered list"



def markdown_to_html_node(text):
    main_node = ParentNode("div", [])
    blocks = markdown_to_blocks(text)
    children = []

    for block in blocks:
        children.append(block_to_html_node(block))

    main_node.children = children

    return main_node        

def markdown_to_blocks(md_text):
    blocks = md_text.split("\n\n")

    blocks = list(map(lambda x: x.strip(), blocks))
    blocks = list(filter(lambda x: x != "", blocks))

    return blocks



def block_to_html_node(block):
    type = block_to_block_type(block)

    match(type):
        case BlockType.PARAGRAPH:
            result = ParentNode("p", [])
            text = reduce_block_to_a_line(block)
            result.children = convert_text_to_html_nodes(text)

        case BlockType.HEADING:
            split_block = block.split(" ", maxsplit=1)
            heading = split_block[0]

            result = ParentNode(f"h{len(heading)}", [])
            text = split_block[1]
            result.children = convert_text_to_html_nodes(text)

        case BlockType.QUOTE:
            result = ParentNode("blockquote", [])
            text = remove_n_chars_from_each_line(block, 1)
            text = reduce_block_to_a_line(text)
            result.children = convert_text_to_html_nodes(text)

        case BlockType.UNORDERED_LIST:
            result = ParentNode("ul", [])
            text = remove_n_chars_from_each_line(block, 2)
            result.children = convert_list_to_html_nodes(text)

        case BlockType.ORDERED_LIST:
            result = ParentNode("ol", [])
            text = remove_n_chars_from_each_line(block, 2)
            result.children = convert_list_to_html_nodes(text)

        case BlockType.CODE:
            text = block.removeprefix("```").removesuffix("```")
            text = text.removeprefix("\n") # Checks for new line at the start
            result = ParentNode("pre", [LeafNode("code", text)])
        
    return result

def reduce_block_to_a_line(block):
    lines = block.split("\n")
    lines = list(map(lambda x: x.strip(), lines))
    text = " ".join(lines)

    return text

def convert_list_to_html_nodes(text):
    lines = text.split("\n")
    children = []

    for line in lines:
        text = line.strip()
        grandchildren = convert_text_to_html_nodes(text)
        children.append(ParentNode("li", grandchildren))

    return children
        
def convert_text_to_html_nodes(text):
    text_nodes = split_nodes(text)
    html_nodes = []

    for node in text_nodes:
        html_nodes.append(text_node_to_html_node(node))

    return html_nodes

def remove_n_chars_from_each_line(text, n):
    split = text.split("\n")
    new_text = []
    for line in split:
        new_text.append(line[n:])
    return "\n".join(new_text)

def text_node_to_html_node(text_node):
    match text_node.text_type:
        case TextType.TEXT:
            return LeafNode(None, text_node.text)
        case TextType.BOLD:
            return LeafNode("b", text_node.text)
        case TextType.ITALIC:
            return LeafNode("i", text_node.text)
        case TextType.CODE:
            return LeafNode("code", text_node.text)
        case TextType.LINK:
            return LeafNode("a", text_node.text, { "href" : text_node.url })
        case TextType.IMAGE:
            return LeafNode("img", text_node.text, { "src" : text_node.url })
        case _:
            raise Exception("Unsupported TextType")



def block_to_block_type(block):
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
