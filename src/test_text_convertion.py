import unittest

from text_convertion import text_node_to_html_node, split_nodes_delimiter
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
        node = TextNode(text, TextType.LINK, "http//mylink")
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag, 'a')
        self.assertEqual(html_node.to_html(), f'<a href="http//mylink">{text}</a>')

    def test_image(self):
        node = TextNode("", TextType.IMAGE, "https//myimage")
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag, 'img')
        self.assertEqual(html_node.to_html(), f'<img src="https//myimage" alt="https//myimage"></img>')


class TestSplitNodesDelimiter(unittest.TestCase):
    def test_code_delimeter(self):
        node = TextNode("This is text with a `code block` word", TextType.TEXT)
        new_nodes = split_nodes_delimiter([node], "`", TextType.CODE)
        self.assertListEqual(
            [
                TextNode("This is text with a ", TextType.TEXT),
                TextNode("code block", TextType.CODE),
                TextNode(" word", TextType.TEXT)
            ],
            new_nodes,
        )

    def test_bold_delimeter(self):
        node = TextNode("This is text with a **bold block** word", TextType.TEXT)
        new_nodes = split_nodes_delimiter([node], "**", TextType.BOLD)
        self.assertListEqual(
            [
                TextNode("This is text with a ", TextType.TEXT),
                TextNode("bold block", TextType.BOLD),
                TextNode(" word", TextType.TEXT)
            ],
            new_nodes,
        )

    def test_italic_delimeter(self):
        node = TextNode("This is text with a _italic block_ word", TextType.TEXT)
        new_nodes = split_nodes_delimiter([node], "_", TextType.ITALIC)
        self.assertListEqual(
            [
                TextNode("This is text with a ", TextType.TEXT),
                TextNode("italic block", TextType.ITALIC),
                TextNode(" word", TextType.TEXT)
            ],
            new_nodes,
        )

    def test_no_delimeter(self):
        node = TextNode("This is text with a no delimeter", TextType.TEXT)
        new_nodes = split_nodes_delimiter([node], "_", TextType.ITALIC)
        self.assertListEqual(
            [
                TextNode("This is text with a no delimeter", TextType.TEXT)
            ],
            new_nodes,
        )
