import re
from enum import Enum


class BlockType(Enum):
    PARAGRAPH = "paragraph"
    HEADING = "heading"
    CODE = "code"
    QUOTE = "quote"
    UNORDERED_LIST = "unordered_list"
    ORDERED_LIST = "ordered_list"


def markdown_to_blocks(markdown):
    sections = markdown.split("\n\n")
    sections = [s.strip() for s in sections if s.strip() != ""]
    return sections


def block_to_block_type(block):
    if re.match(r"^#{1,6}(?!#)", block):
        return BlockType.HEADING
    if block.startswith("```") and block.endswith("```"):
        return BlockType.CODE
    if block.startswith('>'):
        if is_unorder(block, '>'):
            return BlockType.QUOTE
    if block.startswith('-'):
        if is_unorder(block, '-'):
            return BlockType.UNORDERED_LIST
    if block[0].isdigit():
        if is_order(block):
            return BlockType.ORDERED_LIST
    return BlockType.PARAGRAPH


def is_unorder(block, start):
    lines = block.split('\n')
    for line in lines:
        if not line.startswith(start):
            return False
    return True


def is_order(block):
    lines = block.split('\n')
    for line in lines:
        if not re.match(r"^\d+\.\s", line):
            return False
    return True
