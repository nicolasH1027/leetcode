# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: ListNode) -> bool:
        
        dummy = ListNode(0)
        dummy.next = head
        
        while head and head.next:
            head = head.next.next
            dummy = dummy.next
            if head == dummy:
                break
        
        return dummy == head
            
            