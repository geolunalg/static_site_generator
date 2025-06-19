import re

from textnode import TextType, TextNode
from htmlnode import LeafNode


def extract_markdown_images(text):
    regx = r"!\[([^\]]*)\]\((https?:\/\/[^\s)]+)\)"
    results = re.findall(regx, text)
    return results


def extract_markdown_links(text):
    regx = regx = r"\[([^\]]*)\]\((https?:\/\/[^\s)]+)\)"
    results = re.findall(regx, text)
    return results


def split_nodes_image(old_nodes):
    new_nodes = []
    for node in old_nodes:
        if node.text_type != TextType.TEXT:
            new_nodes.append(node)
            continue

        original_text = node.text
        images = extract_markdown_images(original_text)

        for image in images:
            img = f"![{image[0]}]({image[1]})"
            sections = original_text.split(img, 1)

            if len(sections) != 2:
                raise ValueError("invalid markdown, image section not closed")

            if sections[0] != "":
                new_nodes.append(TextNode(sections[0], TextType.TEXT))
            new_nodes.append(TextNode(image[0], TextType.IMAGE, image[1]))
            original_text = sections[1]

        if original_text != "":
            new_nodes.append(TextNode(original_text, TextType.TEXT))

    return new_nodes


def split_nodes_link(old_nodes):
    new_nodes = []
    for node in old_nodes:
        if node.text_type != TextType.TEXT:
            new_nodes.append(node)
            continue

        original_text = node.text
        links = extract_markdown_links(original_text)

        for image in links:
            img = f"[{image[0]}]({image[1]})"
            sections = original_text.split(img, 1)

            if len(sections) != 2:
                raise ValueError("invalid markdown, link section not closed")

            if sections[0] != "":
                new_nodes.append(TextNode(sections[0], TextType.TEXT))
            new_nodes.append(TextNode(image[0], TextType.LINK, image[1]))
            original_text = sections[1]

        if original_text != "":
            new_nodes.append(TextNode(original_text, TextType.TEXT))

    return new_nodes
