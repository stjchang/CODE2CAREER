class Node:
    def __init__(self, data=None):
            self.data = data
            self.next = None
                
class LinkedList:
    def __init__(self):
        self._head = Node() # this head is a dummy node
        self._tail = self._head
    
    def append(self, data):
        dummy = Node(data)
        self._tail.next = dummy
        self._tail = dummy
    
    def length(self):
        curr = self._head
        res = 0
        while curr.next:    
            curr = curr.next
            res += 1
        
        return res
    
    def display(self):
        res = []
        curr = self._head 
        while curr.next:
            curr = curr.next
            res.append(curr.data)

            
        return res

if __name__ == "__main__":
    my_list = LinkedList()
    my_list.append(1)
    my_list.append(2)
    my_list.append(3)

    print("List contents:", my_list.display())
    print("List length:", my_list.length())
    