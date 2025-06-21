from textnode import TextType


class HTMLNode():
    def __init__(self, value=None, tag=None, children=None, props=None):
        self.tag = tag
        self.value = value
        self.children = children
        self.props = props

    def to_html(self):
        raise NotImplementedError("not implemented error")

    def props_to_html(self):
        if self.props is None:
            return ""

        props_string = []
        for key, value in self.props.items():
            string = f'{key}="{value}"'
            props_string.append(string)
        return " " + ' '.join(props_string)

    def __repr__(self):
        return f"HTMLNode({self.tag}, {self.value}, {self.children}, {self.props})"


class LeafNode(HTMLNode):
    def __init__(self, value, tag=None, props=None):
        super().__init__(value, tag, None, props)

    def to_html(self):
        if self.value is None:
            raise ValueError("leaf nodes must have a value")
        if self.tag is None:
            return self.value
        open_tag = f"<{self.tag}{self.props_to_html()}>" if self.tag else ""
        close_tag = f"</{self.tag}>" if self.tag else ""
        return f"{open_tag}{self.value}{close_tag}"


class ParentNode(HTMLNode):
    def __init__(self, tag, children, props=None):
        super().__init__(None, tag, children, props)

    def to_html(self):
        if self.tag is None:
            raise ValueError("parent node must hava a tag")

        if self.children is None:
            raise ValueError("parent must have children")

        open_tag = f"<{self.tag}{self.props_to_html()}>"
        close_tag = f"</{self.tag}>"
        children = []
        for child in self.children:
            children.append(child.to_html())

        return open_tag + ''.join(children) + close_tag
