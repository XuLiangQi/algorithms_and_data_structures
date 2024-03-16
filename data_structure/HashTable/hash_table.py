class HashTable:
    """
    Initialize a hash table with size
        Each element in this hash table contains 
        an 2D array [key, value]. 
    """
    def __init__(self, size: int):
        self.size = size
        self.table = [ [] for _ in range (0, self.size)]

    def hash(self, key: str) -> int:
        """Hash the key value provided while ensuring
        the resulting index falls within the table range
        
        Parameters:
        ----------
            key: String name of the value. 
            
        Returns:
        --------
            The index of the location on hash table.
        """
        return hash(key) % self.size

    def add(self, key: str, value: float):
        """Add a new element [key, value] to
        this hash table.
        Parameters:
        ----------
            key: The string name of the value.
            value: The actual value.
        Returns:
        -------
            None
        """
        hashing = self.hash(key)
        single_array = [key, value]
        self.table[hashing].append(single_array)
    
    def find(self, key: str):
        """Find an element from this hash
        table by searching its key.
        Parameters:
        ----------
            key: The string name of the value.
        Returns:
        --------
            None
        """
        hashing = self.hash(key)
        found_array = self.table[hashing]
        for row in found_array:
             if row[0] == key:
                 print(row[0], row[1])
    
    def delete(self, key: str):
        """Remove an element from this
        hash table by searching
        its key.
        Parameters:
        ----------
            key: The string name of the value.
        Returns:
        --------
            None
        """
        hashing = self.hash(key)
        found_array = self.table[hashing]
        row = 0
        while(row < len(found_array)):
            if found_array[row][0] == key:
                del found_array[row]
            else:
                row += 1


if __name__ == "__main__":
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
