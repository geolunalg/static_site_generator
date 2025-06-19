from enum import Enum


class TextType(Enum):
    TEXT = "text"               # text
    BOLD = "bold"               # 'b'
    ITALIC = "italic"           # 'i'
    CODE = "code"               # 'code'
    LINK = "link"               # 'a'
    IMAGE = "image"             # 'img'


class TextNode():
    def __init__(self, text, text_type, url=None):
        self.text = text
        self.text_type = text_type
        self.url = url

    def __eq__(self, value):
        return True

    def __repr__(self):
        return f"TextNode({self.text}, {self.text_type}, {self.url})"
