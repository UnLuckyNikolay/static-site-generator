from textnode import *
from leafnode import *
from parentnode import *


def main():
    test = TextNode("WATCH OUT FOR THIS **NEW* TRICK!", TextType.TEXT)
    nodes = split_nodes_delimiter([test], '**', TextType.BOLD)
    print(nodes)


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
            return LeafNode("a", text_node.text)
        case TextType.IMAGE:
            return LeafNode("img", text_node.text)
        case _:
            raise Exception("Unsupported TextType")
        

def split_nodes_delimiter(old_nodes, delimiter, text_type):
    new_nodes = []

    for old_node in old_nodes:
        strings = old_node.text.split(delimiter)
        if len(strings) % 2 != 1:
            raise Exception(f"Missing closing delimiter {delimiter}. String: {old_node.text}")

        for i in range(len(strings)):
            if len(strings[i]) == 0:
                continue

            if i % 2 == 1:
                new_nodes.append(TextNode(strings[i], text_type))
            else:
                new_nodes.append(TextNode(strings[i], TextType.TEXT))

    return new_nodes


if __name__ == "__main__":
    main()