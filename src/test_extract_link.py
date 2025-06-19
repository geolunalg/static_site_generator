import unittest

from extract_link import extract_markdown_images, extract_markdown_links, split_nodes_image, split_nodes_link
from textnode import TextNode, TextType


class TestExtractMarkdownImages(unittest.TestCase):
    def test_extract_markdown_images_single(self):
        matches = extract_markdown_images(
            "This is text with an ![image](https://i.imgur.com/zjjcJKZ.png)"
        )
        self.assertListEqual([("image", "https://i.imgur.com/zjjcJKZ.png")], matches)

    def test_extract_markdown_images_multiple(self):
        text = "This is text with a ![rick roll](https://i.imgur.com/aKaOqIh.gif) and ![obi wan](https://i.imgur.com/fJRm4Vk.jpeg)"
        matches = extract_markdown_images(text)
        self.assertListEqual(
            [
                ("rick roll", "https://i.imgur.com/aKaOqIh.gif"),
                ("obi wan", "https://i.imgur.com/fJRm4Vk.jpeg")
            ],
            matches
        )

    def test_extract_markdown_no_images(self):
        text = "This is text with a have none"
        matches = extract_markdown_images(text)
        self.assertListEqual([], matches)


class TestExtractMarkdownLinks(unittest.TestCase):
    def test_extract_markdown_link_single(self):
        matches = extract_markdown_links(
            "This is text with a link [link](https://www.mylink.dev)"
        )
        self.assertListEqual([("link", "https://www.mylink.dev")], matches)

    def test_extract_markdown_link_multiple(self):
        text = "This is text with a link [to boot dev](https://www.boot.dev) and [to youtube](https://www.youtube.com/@bootdotdev)"
        matches = extract_markdown_links(text)
        self.assertListEqual(
            [
                ("to boot dev", "https://www.boot.dev"),
                ("to youtube", "https://www.youtube.com/@bootdotdev")
            ],
            matches
        )

    def test_extract_markdown_no_link(self):
        text = "This is text with no link"
        matches = extract_markdown_links(text)
        self.assertListEqual([], matches)


class TestSplitNodesImage(unittest.TestCase):
    def test_split_images_multiples(self):
        node = TextNode(
            "This is text with an ![image](https://i.imgur.com/zjjcJKZ.png) and another ![second image](https://i.imgur.com/3elNhQu.png)",
            TextType.TEXT,
        )

        results = split_nodes_image([node])
        self.assertListEqual(
            [
                TextNode("This is text with an ", TextType.TEXT),
                TextNode("image", TextType.IMAGE, "https://i.imgur.com/zjjcJKZ.png"),
                TextNode(" and another ", TextType.TEXT),
                TextNode("second image", TextType.IMAGE, "https://i.imgur.com/3elNhQu.png"),
            ],
            results,
        )

    def test_split_images_single(self):
        node = TextNode(
            "![image](https://i.imgur.com/zjjcJKZ.png)",
            TextType.TEXT,
        )

        results = split_nodes_image([node])
        self.assertListEqual(
            [TextNode("image", TextType.IMAGE, "https://i.imgur.com/zjjcJKZ.png")],
            results,
        )

    def test_split_no_images(self):
        node = TextNode(
            "no images here",
            TextType.TEXT,
        )

        results = split_nodes_image([node])
        self.assertListEqual(
            [TextNode("no images here", TextType.TEXT)],
            results
        )


class TestSplitNodesLinks(unittest.TestCase):
    def split_nodes_link_multiples(self):
        node = TextNode(
            "This is text with a link [to boot dev](https://www.boot.dev) and [to youtube](https://www.youtube.com/@bootdotdev)",
            TextType.TEXT,
        )

        results = split_nodes_image([node])
        self.assertListEqual(
            [
                TextNode("This is text with a link ", TextType.TEXT),
                TextNode("to boot dev", TextType.LINK, "https://www.boot.dev"),
                TextNode(" and ", TextType.TEXT),
                TextNode("to youtube", TextType.LINK, "https://www.youtube.com/@bootdotdev")
            ],
            results,
        )

    def split_nodes_link_single(self):
        node = TextNode(
            "[to boot dev](https://www.boot.dev)",
            TextType.TEXT,
        )

        results = split_nodes_image([node])
        self.assertListEqual(
            [TextNode("to boot dev", TextType.LINK, "https://www.boot.dev")],
            results,
        )

    def split_nodes_no_link(self):
        node = TextNode(
            "no links here",
            TextType.TEXT,
        )

        results = split_nodes_image([node])
        self.assertListEqual(
            [TextNode("no links here", TextType.TEXT)],
            results,
        )
