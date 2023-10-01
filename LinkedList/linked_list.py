class Node:
    def __init__(self, value):
        self.value = value
        self.next_node = None

class LinkedList:
    def __init__(self):
        self.head = None

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
    


ls = LinkedList()
ls.add(5)
ls.add(3)
ls.add(1)    
ls.add(2)       
ls.show()     