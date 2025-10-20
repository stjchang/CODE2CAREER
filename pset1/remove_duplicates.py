# Problem 4: Given an unsorted singly linked list, remove all duplicate nodes from the list.

class ListNode:
    def __init__ (self, data):
        self.data = data
        self.next = None
        
def remove_duplicates(head: ListNode) -> ListNode:
    dummy = head
    seen = set()
    
    while head.next:
        seen.add(head.data)
        
        if head.next.data in seen:
            head.next = head.next.next
        else:
            head = head.next
    
    return dummy.next
    
    
    
    