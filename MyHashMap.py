class ListNode:
    def __init__(self, key=None, val=None):
        self.key = key
        self.val = val
        self.next = None

class MyHashMap:    
#   using a Linked_List
    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.nodes = [ListNode() for i in range(10000)]
        
    def hashFunction(self, key: int) -> int:
        """
        Hash function logic
        """
        return key%len(self.nodes)
        
    def put(self, key: int, value: int) -> None:
        """
        value will always be non-negative.
        """
        # if key not in self.map:
        #     self.map[key] = Node(val)
        # else:
        #     linkedListHead = self.map.get(key)
        #     while linkedListHead and linkedListHead.next:
        #         linkedListHead = linkedListHead.next
        #     linkedListHead.next = Node(val)
        index = self.hashFunction(key)
        prev = self.find(index, key)
        if prev.next == None:
            prev.next = ListNode(key, value)
        else:
            prev.next.val = value
                
            
    def get(self, key: int) -> int:
        """
        Returns the value to which the specified key is mapped, or -1 if this map contains no mapping for the key
        """
        index = self.hashFunction(key)
        prev = self.find(index, key)
        if prev.next is None:
            return -1
        else:
            return prev.next.val
        
       
        
    def find(self, index: int, key: int) -> None:
        """
        Find the value
        """
        if self.nodes[index] == None:
            node[index] =  ListNode(-1, -1)
            return node[index]
        else:
            prev = self.nodes[index]
            while prev.next is not None and prev.next.key != key:
                prev = prev.next
        return prev
            
        
    def remove(self, key: int) -> None:
        """
        Removes the mapping of the specified value key if this map contains a mapping for the key
        """
        index = self.hashFunction(key)
        prev = self.find(index, key)
        if self.nodes[index] != None and prev.next is not None:
            prev.next = prev.next.next
        
        


# Your MyHashMap object will be instantiated and called as such:
# obj = MyHashMap()
# obj.put(key,value)
# param_2 = obj.get(key)
# obj.remove(key)