class Node(object):
    def __init__(self,value):
        self.value = value
        self.right = None
        self.left = None

class Binary_tree(object):
    def __init__(self, root):
        self.root = Node(root)