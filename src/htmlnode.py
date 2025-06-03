class HTMLNode():
    def __init__(self, tag=None, value=None, children=None, props=None):
        self.tag = tag
        self.value = value
        self.children = children
        self.props = props
    
    def __eq__(self, node):
        return (self.tag == node.tag and
                self.value == node.value and
                self.children == node.children and
                self.props == node.props)
    
    def __repr__(self):
        return f"HTMLNode({self.tag}, {self.value}, {self.children}, {self.props})"

    def to_html(self):
        raise NotImplementedError
    
    def props_to_html(self):
        result = ""
        if self.props != None:
            for pair in self.props.items():
                result += f" {pair[0]}=\"{pair[1]}\""
        return result