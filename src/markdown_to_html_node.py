from markdown_to_blocks import markdown_to_blocks, block_to_block_type, BlockType
from text_convertion import text_node_to_html_node
from text_to_textnodes import text_to_textnodes
from textnode import TextNode, TextType
from htmlnode import ParentNode


def markdown_to_html_node(markdown):
    blocks = markdown_to_blocks(markdown)
    children = []
    for block in blocks:
        child = block_to_html_node(block)
        children.append(child)
    return ParentNode("div", children)


def block_to_html_node(block):
    type = block_to_block_type(block)
    match type:
        case BlockType.PARAGRAPH:
            return paragraph_to_html_node(block)
        case BlockType.CODE:
            return code_to_html_node(block)
        case BlockType.HEADING:
            return heading_to_html_node(block)
        case BlockType.QUOTE:
            return quote_to_html_node(block)
        case BlockType.UNORDERED_LIST:
            return unordered_list_to_html_node(block)
        case BlockType.ORDERED_LIST:
            return ordered_list__to_html_node(block)
            pass
        case _:
            raise ValueError("incorrect block type")


def text_to_children(text):
    nodes = text_to_textnodes(text)
    children = []
    for node in nodes:
        child = text_node_to_html_node(node)
        children.append(child)
    return children


def paragraph_to_html_node(block):
    lines = block.split('\n')
    text = ' '.join(lines)
    children = text_to_children(text)
    return ParentNode('p', children)


def code_to_html_node(block):
    if not block.startswith("```") and not block.endswith("```"):
        raise ValueError("invalid code block")
    text = block[3:-3].strip()
    text_node = TextNode(text, TextType.TEXT)
    code = text_node_to_html_node(text_node)
    child = ParentNode("code", [code])
    return ParentNode("pre", [child])


def heading_to_html_node(block):
    hlevel = 0
    while block[hlevel] == '#':
        hlevel += 1
    if hlevel + 1 >= len(block):
        raise ValueError(f"invalid heading level h: {hlevel}")
    text = block[hlevel + 1:]
    children = text_to_children(text)
    return ParentNode(f"h{hlevel}", children)


def quote_to_html_node(block):
    lines = block.split('\n')
    quotes = []
    for line in lines:
        if not line.startswith('>'):
            raise ValueError("quotes must start with '>'")
        quotes.append(line.lstrip('>').strip())
    full_quote = " ".join(quotes)
    children = text_to_children(full_quote)
    return ParentNode("blockquote", children)


def unordered_list_to_html_node(block):
    lines = block.split("\n")
    ulist = []
    for line in lines:
        text = line[1:].strip()
        children = text_to_children(text)
        ulist.append(ParentNode("li", children))
    return ParentNode("ul", ulist)


def ordered_list__to_html_node(block):
    lines = block.split("\n")
    olist = []
    for line in lines:
        text = line[line.index(" "):].strip()
        children = text_to_children(text)
        olist.append(ParentNode("li", children))
    return ParentNode("ol", olist)
