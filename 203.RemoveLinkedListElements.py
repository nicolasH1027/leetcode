# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
        
        dummy = ListNode(next = head)
        
        cur = dummy
        
        while cur and cur.next:
            while cur.next.val == val:
                cur.next = cur.next.next
                if not cur.next:
                    break
            cur = cur.next
        
        return dummy.next
    

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
        
        dummy = ListNode(next = head)
        
        prev, cur = dummy, head
        
        while cur:
            
            if cur.val == val:
                prev.next = cur.next
            else:
                prev = cur
            
            cur = cur.next
        
        return dummy.next