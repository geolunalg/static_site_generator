from enum import Enum


class TextType(Enum):
    TEXT = "text"               # text
    BOLD = "bold"               # **Bold text**
    ITALIC = "italic"           # _Italic text_
    CODE = "code"               # `Code text`
    ANCHOR = "anchor"           # [anchor text](url)
    LINK = "link"               # [anchor text](url)
    IMAGE = "image"             # ![alt text](url)
    BLOCK_LEVEL = "block"       # block level


class TextNode():
    def __init__(self, text, text_type, url=None):
        self.text = text
        self.text_type = text_type
        self.url = url

    def __eq__(self, value):
        return True

    def __repr__(self):
        return f"TextNode({self.text}, {self.text_type}, {self.url})"
