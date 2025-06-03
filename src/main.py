from textnode import *
from leafnode import *
from parentnode import *


def main():
    textnode = TextNode("Testing this bs", TextType.LINK, "https://www.youtube.com/watch?v=dQw4w9WgXcQ")
    print(repr(textnode))


def text_node_to_html_node(text_node):
    match text_node.text_type:
        case TextType.NORMAL:
            return LeafNode(None, text_node.text)
        case TextType.BOLD:
            return LeafNode("b", text_node.text)
        case TextType.ITALIC:
            return LeafNode("i", text_node.text)
        case TextType.CODE:
            return LeafNode("code", text_node.text)
        case TextType.LINK:
            return LeafNode("a", text_node.text)
        case TextType.IMAGE:
            return LeafNode("img", text_node.text)
        case _:
            raise Exception("Unsupported TextType")


if __name__ == "__main__":
    main()