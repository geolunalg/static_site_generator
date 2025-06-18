import unittest

from textnode import TextNode, TextType


class TestTextNode(unittest.TestCase):
    def test_eq(self):
        node = TextNode("This is a text node", TextType.BOLD)
        node2 = TextNode("This is a text node", TextType.BOLD)
        self.assertEqual(node, node2)

    def test_repr(self):
        text = "This is a text node"
        type = TextType.BOLD
        url = "https://myaddress"
        node = TextNode(text, type, url)
        self.assertEqual(node.__repr__(), f"TextNode({text}, {type}, {url})")

    def test_optional_url(self):
        url = "https://myaddress"
        node = TextNode("This is a text node", TextType.BOLD)
        node2 = TextNode("This is a text node", TextType.BOLD, url)
        self.assertEqual(node, node2)
        self.assertEqual(None, node.url)
        self.assertEqual(url, node2.url)

    def test_different_text_types(self):
        node = TextNode("This is a text node", TextType.ITALIC)
        node2 = TextNode("This is a text node", TextType.BOLD)
        self.assertNotEqual(node.text_type, node2.text_type)


if __name__ == "__main__":
    unittest.main()
