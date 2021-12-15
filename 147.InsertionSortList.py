# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def insertionSortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        
        dummy = ListNode(-5001)
        jump = dummy
        tmp = head

        
        while tmp:
            
            cur = tmp
            
            tmp = cur.next
            
            prev = None
            while jump and jump.val <= cur.val:
                prev = jump
                jump = jump.next
                
            prev.next = cur
            cur.next = jump
            jump = dummy

                
        return dummy.next