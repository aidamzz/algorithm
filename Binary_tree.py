class Node(object):
    def __init__(self,value):
        self.value = value
        self.right = None
        self.left = None

class Binary_tree(object):
    def __init__(self, root):
        self.root = Node(root)
    def print_tree(self, traversal_type):
        if traversal_type == 'preorder':
            return self.preorder_print(tree.root, "")
        else:
            print("Traversal type "+ str(traversal_type)+ " is not supported.")
    def preorder_print(self, start, traversal):
        if start:
            traversal += (str(start.value)+ "-")
            traversal = self.preorder_print(start.left, traversal)
            traversal = self.preorder_print(start.right, traversal)
        return traversal