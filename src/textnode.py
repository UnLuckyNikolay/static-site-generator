from enum import Enum

class TextType(Enum):
    TEXT_NORMAL = "normal"
    TEXT_BOLD = "bold"
    TEXT_ITALIC = "italic"
    TEXT_CODE = "code"
    TEXT_LINK = "link"
    TEXT_IMAGE = "image"

class TextNode():
    def __init__(self, text, text_type, url=None):
        self.text = text
        self.text_type = text_type
        self.url = url
    
    def __eq__(self, textnode):
        return textnode.text == self.text and textnode.text_type == self.text_type and textnode.url == self.url
    
    def __repr__(self):
        return f"TextNode({self.text}, {self.text_type.value}, {self.url})"
