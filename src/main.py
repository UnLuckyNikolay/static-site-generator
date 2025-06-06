from textnode import *
from leafnode import *
from parentnode import *


def main():
    test = TextNode("WATCH OUT FOR THIS **NEW** TRICK!", TextType.TEXT)
    nodes = split_nodes_delimiter([test], '**')
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
        

def split_nodes_delimiter(old_nodes, delimiter):
    delimeters = ['`', '**', '_']
    text_types = [TextType.CODE, TextType.BOLD, TextType.ITALIC]
    new_nodes = []
    
    if delimiter not in delimeters:
        raise Exception(f"Invalid delimiter {delimiter}.")
    
    if isinstance(old_nodes, TextNode):
        old_nodes = [old_nodes]

    for old_node in old_nodes:
        if old_node.text_type != TextType.TEXT: # For now only splits plain text, if changed - remove test_not_plain_text in test_textnode.TestSplitNodes
            new_nodes.append(old_node)
            continue

        strings = old_node.text.split(delimiter)
        if len(strings) % 2 != 1:
            raise Exception(f"Missing closing delimiter {delimiter}. String: {old_node.text}")

        for i in range(len(strings)):
            if len(strings[i]) == 0: # Remove this to keep empty nodes, also remove test_bold_at_the_start in test_textnode.TestSplitNodes
                continue

            if i % 2 == 1:
                new_nodes.append(TextNode(strings[i], text_types[delimeters.index(delimiter)]))
            else:
                new_nodes.append(TextNode(strings[i], TextType.TEXT))

    return new_nodes


if __name__ == "__main__":
    main()