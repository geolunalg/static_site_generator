from textnode import TextType
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
        case '_':
            return
