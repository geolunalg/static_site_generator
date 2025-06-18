import unittest

from htmlnode import HTMLNode, LeafNode, ParentNode


class TestHTMLNode(unittest.TestCase):
    def test_none_props(self):
        node = HTMLNode()
        result = node.props_to_html()
        self.assertEqual("", result)

    def test_props_string(self):
        props = {"one": "one", "two": "two"}
        node = HTMLNode(props=props)
        result = node.props_to_html()
        self.assertEqual(' one="one" two="two"', result)

    def test_to_html(self):
        node = HTMLNode()
        self.assertRaises(NotImplementedError, node.to_html)


class TestLeafNode(unittest.TestCase):
    def test_leaf_to_html_p(self):
        node = LeafNode("Hello, world!", "p")
        self.assertEqual(node.to_html(), "<p>Hello, world!</p>")

    def test_leaf_to_html_p_with_props(self):
        node = LeafNode("Hello, world!", "p", {"one": "one", "two": "two"})
        self.assertEqual(node.to_html(), '<p one="one" two="two">Hello, world!</p>')

    def test_leaf_to_html_no_tag(self):
        node = LeafNode("Hello, world!")
        self.assertEqual(node.to_html(), "Hello, world!")


class TestParentNode(unittest.TestCase):
    def test_to_html_with_children(self):
        child_node = LeafNode("child", "span")
        parent_node = ParentNode("div", [child_node])
        self.assertEqual(parent_node.to_html(), "<div><span>child</span></div>")

    def test_to_html_with_grandchildren(self):
        grandchild_node = LeafNode("grandchild", "b")
        child_node = ParentNode("span", [grandchild_node])
        parent_node = ParentNode("div", [child_node])
        self.assertEqual(
            parent_node.to_html(),
            "<div><span><b>grandchild</b></span></div>",
        )

    def test_to_html_value_error_no_tag(self):
        child_node = LeafNode("child", "b")
        parent_node = ParentNode("", [child_node])
        self.assertRaises(ValueError, parent_node.to_html)

    def test_to_html_value_error_child_no_value(self):
        child_node = LeafNode("", "b")
        parent_node = ParentNode("div", [child_node])
        self.assertRaises(ValueError, parent_node.to_html)
