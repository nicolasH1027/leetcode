# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
from typing import Counter


class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        "Recursion, the return value is thr root after reverse, the reverse process is done without returning anything"
        if not head or not head.next:
            return head
        
        root = self.reverseList(head.next)
        
        head.next.next = head
        head.next = None
        
        return root
    

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        "Iterative method"
        cur = head
        newhead = None
        while cur:
            tmp = cur.next
            cur.next = newhaed
            newhead = cur
            cur = tmp            
        return newhead