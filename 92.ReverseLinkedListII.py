# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        "Iterative"
        "two pointer, same with 206"
        dummy = ListNode()
        dummy.next = head
        
        lpt = dummy
        
        while left > 1:
            lpt = lpt.next
            left -= 1
            right -= 1
            
        newhead = None
        cur = lpt.next
        rev_tail = lpt. next
        
        while right:
            
            tmp = cur.next
            cur.next = newhead
            newhead = cur
            cur = tmp
            right -= 1
        
        lpt.next = newhead
        rev_tail.next = tmp
        return dummy.next        

class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        "Recursion,  instead of reversing the list, we can just swap the value"
        