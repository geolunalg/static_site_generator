import unittest

from text_to_html import text_node_to_html_node
from textnode import TextType, TextNode


class TestTextToHTML(unittest.TestCase):
    def test_text(self):
        text = "This is a text node"
        node = TextNode(text, TextType.TEXT)
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag, None)
        self.assertEqual(html_node.value, text)

    def test_bold(self):
        text = "This is a bold node"
        node = TextNode(text, TextType.BOLD)
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag, 'b')
        self.assertEqual(html_node.to_html(), f"<b>{text}</b>")

    def test_italic(self):
        text = "This is a italic node"
        node = TextNode(text, TextType.ITALIC)
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag, 'i')
        self.assertEqual(html_node.to_html(), f"<i>{text}</i>")

    def test_code(self):
        text = "This is a code node"
        node = TextNode(text, TextType.CODE)
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag, 'code')
        self.assertEqual(html_node.to_html(), f"<code>{text}</code>")

    def test_link(self):
        text = "This is a link node"
        node = TextNode(text, TextType.LINK, "http:\\mylink")
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag, 'a')
        self.assertEqual(html_node.to_html(), f'<a href="http:\\mylink">{text}</a>')

    def test_image(self):
        node = TextNode("", TextType.IMAGE, "https:\\myimage")
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag, 'img')
        self.assertEqual(html_node.to_html(), f'<img src="https:\\myimage" alt="https:\\myimage"></img>')
