from textnode import TextType, TextNode
from htmlnode import LeafNode


def text_node_to_html_node(text_node):
    match text_node.text_type:
        case TextType.TEXT:
            return LeafNode(text_node.text)
        case TextType.BOLD:
            return LeafNode(text_node.text, 'b')
        case TextType.ITALIC:
            return LeafNode(text_node.text, 'i')
        case TextType.CODE:
            return LeafNode(text_node.text, 'code')
        case TextType.LINK:
            return LeafNode(text_node.text, 'a', {"href": text_node.url})
        case TextType.IMAGE:
            return LeafNode("", "img", {"src": text_node.url, "alt": text_node.url})
        case _:
            raise ValueError("error: TextType unknow")


def split_nodes_delimiter(old_nodes, delimiter, text_type):
    new_nodes = []
    for node in old_nodes:
        if node.text_type != TextType.TEXT:
            new_nodes.append(node)
            continue

        sections = node.text.split(delimiter)
        if len(sections) % 2 == 0:
            raise ValueError(f"error: {delimiter} has no closing match")

        split_nodes = []
        for i, val in enumerate(sections):
            if val == "":
                continue

            if i % 2 != 0:
                split_nodes.append(TextNode(val, text_type))
            else:
                split_nodes.append(TextNode(val, TextType.TEXT))

        new_nodes.extend(split_nodes)

    return new_nodes
