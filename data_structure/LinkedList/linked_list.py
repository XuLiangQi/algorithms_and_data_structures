"""
Node class contains:
    value: The value of this element.
    next_node: The next node linked to the 
                current node.
"""
class Node:
    def __init__(self, value: int):
        self.value = value
        self.next_node = None

"""
Singly linked list
"""
class LinkedList:
    def __init__(self):
        self.head = None

    def add(self, value: int):
        """Add a new element to this linked list.
        Parameteres:
        ------------
            value: The value to be added to the linked list.

        Returns:
        --------
            None
        """
        new_node = Node(value)
        # When the head is empty, assign the new node
        if self.head == None:
            self.head = new_node
        else:
            current_node = self.head
            # Loop to locate the last element with none
            while True:
                # Loop through all nodes until the next_node is None
                #   which means it is the last node assigned.
                if current_node.next_node != None:
                    current_node = current_node.next_node
                # If None found, then break out this while loop
                else:
                    break
            # Assign the next_node to the current_node of the current_node
            current_node.next_node = new_node

    def show(self):
        """Print out all nodes in this linked list.
        """
        # Start from the head (begining)
        current_node = self.head
        # Loop through and stop when next_node is None
        while current_node.next_node != None:
            print(current_node.value, end=" -> ")
            # Update the "current_node" to be the next_node
            current_node = current_node.next_node
        # Print the last node
        print(current_node.value, " -> None")
    
    def delete(self, value: int):    
        """Remove an element from this linked list.
        Assign the previous node's next_node
        to be the next_node of the removed node.

        Parameters:
        ----------
            value: Value to be removed from the linked list.

        Returns:
        --------
            None
        """
        # Initiate previous_node (to the current_node)
        #   current_node
        #   next_node (to the current_node)
        #   and update them correspondingly
        previous_node = self.head
        current_node = self.head
        next_node = self.head
        while current_node.value != None:
            if (current_node.value == value):
                break
            previous_node = current_node
            current_node = current_node.next_node
            next_node = current_node.next_node
        previous_node.next_node = next_node
        # There is no need to manually free up memory
        #   since Python does it automatically

"""
A node structure that holdes links to 
    the previous node, its own value, 
    and the next node.
"""
class DoublyNode:
    def __init__(self, value: int):
        self.value = value
        self.previous_node = None
        self.next_node = None

"""
Operations related to doubly linked list.
"""
class DoublyLinkedList:
    def __init__(self):
        self.head = None
    
    """
    Add a new element to the doubly linked 
        list.
    """
    def add(self, value):
        this_node = DoublyNode(value)
        if self.head == None:
            self.head = this_node
        else:
            current_node = self.head
            while current_node.next_node is not None:
                current_node = current_node.next_node
            this_node.previous_node = current_node
            current_node.next_node = this_node

    """
    Show the doubly linked list in both
        directions.
    """
    def show(self):
        print("Showing order to the right -> :")
        print("")
        current_node = self.head
        while current_node.next_node is not None:
            print(current_node.value, end=" -> ")
            current_node = current_node.next_node
        print(current_node.value, end=" -> None ")
        print("")
        print("\nShowing order to the left <- :")
        print("")
        while current_node.previous_node is not None:
            print(current_node.value, end=" -> ")
            current_node = current_node.previous_node
        print(current_node.value, end=" -> None")
        print("")

    """
    Deleting an element from the doubly
        linked list.
    """
    def delete(self, value: int):
        previous_node = self.head
        current_node = self.head
        next_node = self.head
        while current_node.next_node is not None:
            if (current_node.value == value):
                break
            previous_node = current_node
            current_node = current_node.next_node
            next_node = current_node.next_node
        # Update both previous and next node after removal
        previous_node.next_node = next_node
        next_node.previous_node = previous_node

"""
Unit tester for linked list related operations.
"""
def test_linked_list(str):
    ls = None
    if str == "Singly":
        print("")
        print("   -- Testing Singly Linked List -- ")
        print("")
        ls = LinkedList()
    elif str == "Doubly":
        print("")
        print("   -- Testing Doubly Linked List -- ")
        print("")
        ls = DoublyLinkedList()
    else:
        print("Wrong input type (Singly or Doubly). ")
        return
    print(" - Adding element : 5")
    ls.add(5)
    print(" - Adding element : 3")
    ls.add(3)
    print(" - Adding element : 1")
    ls.add(1)
    print(" - Adding element : 2")
    ls.add(2)
    print("")
    print(" - Displaying the", str, "Linked List")
    print("")
    ls.show()
    print("")
    print(" - Deleting element : 1")
    ls.delete(1)
    print("")
    print(" - Displaying the", str, "Linked List")
    print("")
    ls.show()

# Testing operations in both singly and doubly linked list
test_linked_list("Singly")
test_linked_list("Doubly")