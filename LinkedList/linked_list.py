"""
Node class contains:
    value: The value of this element.
    next_node: The next node linked to the 
                current node.
"""
class Node:
    def __init__(self, value):
        self.value = value
        self.next_node = None

"""
Singly linked list
"""
class LinkedList:
    def __init__(self):
        self.head = None

    """
    Add a new element to this linked list.
    """
    def add(self, value):
        new_node = Node(value)
        # When the head is empty, assign the new node
        if self.head == None:
            self.head = new_node
        else:
            current_node = self.head
            # Loop to locate the last element with none
            while True:
                # If no None, then go to the next "current_node"
                if current_node.next_node != None:
                    current_node = current_node.next_node
                # If None found, then break out this while loop
                else:
                    break
            # Assign the next_node to the current_node of the current_node
            current_node.next_node = new_node

    """
    Print out all nodes in this linked list.
    """
    def show(self):
        # Start from the head (begining)
        current_node = self.head
        # Loop through and stop when next_node is None
        while current_node.next_node != None:
            print(current_node.value, end=" -> ")
            # Update the "current_node" to be the next_node
            current_node = current_node.next_node
        # Print the last node
        print(current_node.value, " -> None")
    
    """
    Remove an element from this linked list.
        Assign the previous node's next_node
        to be the next_node of the removed node.
    """
    def delete(self, value):
        current_node = self.head
        prev_node = self.head
        next_node = self.head
        while current_node.value != None:
            prev_node = current_node
            current_node = current_node.next_node
            next_node = current_node.next_node
            if (current_node.value == value):
                break
        prev_node.next_node = next_node
        
def test_singly_linked():
    ls = LinkedList()
    ls.add(5)
    ls.add(3)
    ls.add(1)
    ls.add(2)
    ls.show()
    ls.delete(1)
    ls.show()

test_singly_linked()