import unittest

from markdown_to_blocks import markdown_to_blocks, block_to_block_type, BlockType


class TestMarkdownToBlocks(unittest.TestCase):
    def test_markdown_to_blocks(self):
        md = """
This is **bolded** paragraph

This is another paragraph with _italic_ text and `code` here
This is the same paragraph on a new line

- This is a list
- with items
"""
        blocks = markdown_to_blocks(md)
        self.assertEqual(
            blocks,
            [
                "This is **bolded** paragraph",
                "This is another paragraph with _italic_ text and `code` here\nThis is the same paragraph on a new line",
                "- This is a list\n- with items",
            ],
        )

    def test_markdown_to_blocks_multiple_empty_spaces(self):
        md = """
This is **bolded** paragraph



This is another paragraph with _italic_ text and `code` here
This is the same paragraph on a new line



- This is a list
- with items


"""
        blocks = markdown_to_blocks(md)
        self.assertEqual(
            blocks,
            [
                "This is **bolded** paragraph",
                "This is another paragraph with _italic_ text and `code` here\nThis is the same paragraph on a new line",
                "- This is a list\n- with items",
            ],
        )


class BlockToBlockType(unittest.TestCase):
    def test_block_to_block_type_paragraph(self):
        self.assertEqual(block_to_block_type("just a paragraph"), BlockType.PARAGRAPH)

    def test_block_to_block_type_header(self):
        headers = [('#' * (i + 1)) for i in range(7)]
        for header in headers[:-1]:
            self.assertEqual(block_to_block_type(header), BlockType.HEADING)
        self.assertEqual(block_to_block_type(headers[-1]), BlockType.PARAGRAPH)

    def test_block_to_block_type_code(self):
        self.assertEqual(block_to_block_type('```'), BlockType.CODE)
        self.assertEqual(block_to_block_type('``'), BlockType.PARAGRAPH)
        self.assertEqual(block_to_block_type('`'), BlockType.PARAGRAPH)

    def test_block_to_block_type_quote(self):
        quotes = [f"> {i + 1}" for i in range(3)]
        self.assertEqual(block_to_block_type('\n'.join(quotes)), BlockType.QUOTE)

    def test_block_to_block_type_unorder(self):
        unorder = [f"- {i + 1}" for i in range(5)]
        self.assertEqual(block_to_block_type('\n'.join(unorder)), BlockType.UNORDERED_LIST)

    def test_block_to_block_type_order(self):
        order = [f"{i}. {i + 1}" for i in range(2)]
        order += [f"{i + 1}. {i + 1}" for i in range(10, 12)]
        order += [f"{i}. {i}" for i in [101, 1001, 10001]]
        self.assertEqual(block_to_block_type('\n'.join(order)), BlockType.ORDERED_LIST)
