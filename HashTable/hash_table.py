class HashTable:
    """
    Initialize a hash table with size
        Each element in this hash table contains 
        an 2D array [key, value]. 
    """
    def __init__(self, size):
        self.size = size
        self.table = [ [] for _ in range (0, self.size)]

    """
    Add a new element [key, value] to
        this hash table.
    """
    def add(self, key, value):
        hashing = hash(key) % self.size
        single_array = [key, value]
        self.table[hashing].append(single_array)
    
    """
    Find an element from this hash
        table by searching its key.
    """
    def find(self, key):
        hashing = hash(key) % self.size
        found_array = self.table[hashing]
        for row in found_array:
             if row[0] == key:
                 print(row[0], row[1])
    
    """
    Remove an element from this
        hash table by searching
        its key.
    """
    def delete(self, key):
        hashing = hash(key) % self.size
        found_array = self.table[hashing]
        row = 0
        while(row < len(found_array)):
            if found_array[row][0] == key:
                del found_array[row]
            else:
                row += 1

"""
Create a unit tester
"""
def test():
    t = HashTable(5)
    print(t.table)
    t.add("Apple", 0.67)
    t.add("Banana", 0.35)
    t.add("Cherry", 8.99)
    t.add("Damson", 4.99)
    t.add("Figs", 3.99)
    print(t.table)
    t.find("Banana")
    t.delete("Damson")
    t.delete("Figs")
    print(t.table)

test()