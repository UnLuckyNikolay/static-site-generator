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



class ParentNode(HTMLNode):
    def __init__(self, tag, children, props=None):
        super().__init__(tag, None, children, props)    
        
    def __repr__(self):
        return f"ParentNode({self.tag}, {self.children}, {self.props})"

    def to_html(self):
        if self.tag == None:
            raise ValueError("Parent: missing tag")
        if self.children == None:
            raise ValueError("Parent: missing children")
        
        children_to_html = ""
        for child in self.children:
            children_to_html += child.to_html()
                
        result = f"<{self.tag}{self.props_to_html()}>{children_to_html}</{self.tag}>"

        return result



class LeafNode(HTMLNode):
    def __init__(self, tag, value, props=None):
        super().__init__(tag, value, None, props)

    def to_html(self):
        if self.value == None:
            raise ValueError
        if self.tag == None:
            return self.value
        return f"<{self.tag}{self.props_to_html()}>{self.value}</{self.tag}>"
    