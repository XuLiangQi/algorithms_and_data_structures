class Node:
    def __init__(self, value):
        self.left_node = None      # Smaller
        self.right_node = None      # Larger
        self.value = value

class BinaryTree:
    def __init__(self, value):
        self.root = None

    def assign_node(self, node, value):
        new_node = Node(value)
        if node.value is None:
            node.value = value
        elif value > node.value:
            node.right_node = new_node


    def add(self,value):
        this_node = Node(value)
        if self.root is None:
            self.root = this_node
        else:
            current_node = self.root