# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        
        slow = fast = head
        
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            
        prev, cur = ListNode(), slow
        
        while cur:
            tmp = cur.next
            cur.next = prev.next
            prev.next = cur
            cur = tmp
        
        first, second = head, prev.next
        
        while second.next:
            
            tmp = first.next
            first.next = second
            first = tmp
            
            tmp = second.next
            second.next = first
            second = tmp
        
        
            
            
            
            