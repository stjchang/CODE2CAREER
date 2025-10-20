
            
    

class LinkedList:
    class Node:
        def __init__(self, value, next=None):
                self.value = value
                self.next = next
        
        def get(self, index):
            if index >= 0:
                for _ in range(index):
                    self = self.next
                    if not self:
                        break
                return self 
    
    def __init__(self):
        self._head = None
        self._tail = None
        self._length = 0
    
    def isempty(self):
        return self._length == 0

        