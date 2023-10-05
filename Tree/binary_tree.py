class Node:
    def __init__(self, value):
        self.left_node = None      # Smaller
        self.right_node = None      # Larger
        self.value = value

class BinaryTree:
    def __init__(self):
        self.root = None

    def assign_node(self, root_node, new_node):
        if new_node.value > root_node.value:
            if root_node.right_node is None:
                root_node.right_node = new_node
            else:
                self.assign_node(root_node.right_node, new_node)
        else:
            if root_node.left_node is None:
                root_node.left_node = new_node
            else:
                self.assign_node(root_node.left_node, new_node)


    def add(self, value):
        this_node = Node(value)
        if self.root is None:
            self.root = this_node
        else:
            self.assign_node(self.root, this_node)



b = BinaryTree()
b.add(5)
b.add(3)
b.add(7)
b.add(1)
b.add(9)