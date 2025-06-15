import re

from textnode import TextNode, TextType


def markdown_to_blocks(input):
    blocks = input.split("\n\n")

    blocks = list(map(lambda x: x.strip(), blocks))
    blocks = list(filter(lambda x: x != "", blocks))

    return blocks



def split_nodes(input):

    if isinstance(input, str):
        new_nodes = [TextNode(input, TextType.TEXT)]
    elif isinstance(input, TextNode):
        new_nodes = [input]
    elif isinstance(input, list):
        new_nodes = input.copy()
    else:
        raise Exception("Function split_nodes only accepts strings, TextNodes or lists")

    new_nodes = split_nodes_by_type(new_nodes, TextType.IMAGE)
    new_nodes = split_nodes_by_type(new_nodes, TextType.LINK)
    new_nodes = split_nodes_by_type(new_nodes, TextType.BOLD)
    new_nodes = split_nodes_by_type(new_nodes, TextType.ITALIC)
    new_nodes = split_nodes_by_type(new_nodes, TextType.CODE)

    return new_nodes



def split_nodes_by_type(old_nodes, text_type):
    delimiter_types = [TextType.CODE, TextType.BOLD, TextType.ITALIC]
    delimiters =      ['`',           '**',          '_']

    re_types =  [TextType.LINK,               TextType.IMAGE]
    re_target = [r"(?<!!)\[(.*?)\]\((.*?)\)", r"!\[(.*?)\]\((.*?)\)"]
    re_text =   [r"(?<!!)\[.*?\]\(.*?\)",     r"!\[.*?\]\(.*?\)"]

    new_nodes = []

    if isinstance(old_nodes, TextNode):
        old_nodes = [old_nodes]
    
    match text_type:

        case TextType.CODE | TextType.BOLD | TextType.ITALIC:

            delimiter = delimiters[delimiter_types.index(text_type)]

            for old_node in old_nodes:
                #if old_node.text_type != TextType.TEXT: # For now only splits plain text
                #    new_nodes.append(old_node)
                #    continue

                if old_node.text_type == TextType.IMAGE or old_node.text_type == TextType.LINK:
                    new_nodes.append(old_node)
                    continue

                strings = old_node.text.split(delimiter)
                if len(strings) % 2 != 1:
                    raise Exception(f"Missing closing delimiter {delimiter}. String: {old_node.text}")

                for i in range(len(strings)):
                    if len(strings[i]) == 0: # Remove this to keep empty nodes
                        continue

                    if i % 2 == 1:
                        new_nodes.append(TextNode(strings[i], delimiter_types[delimiters.index(delimiter)]))

                    else:
                        new_nodes.append(TextNode(strings[i], old_node.text_type, old_node.url))

        case TextType.LINK | TextType.IMAGE:

            index = re_types.index(text_type)

            for old_node in old_nodes:
                target = re.findall(re_target[index], old_node.text)
                rest = re.split(re_text[index], old_node.text)

                for i in range(len(target) + len(rest)):
                    if i % 2 == 0:
                        if rest[int(i/2)] != "":
                            new_nodes.append(TextNode(rest[ int(i/2) ], old_node.text_type, old_node.url))
                    
                    else:
                        new_nodes.append(TextNode(target[ int((i-1)/2) ][0], text_type, target[ int((i-1)/2) ][1]))

        case _:
            raise Exception("Invalid TextType")

    return new_nodes
