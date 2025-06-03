from htmlnode import HTMLNode

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