# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> ListNode:
        
        pt1, pt2 = headA, headB
        
        while pt1 != pt2:
            
            if not pt1:
                pt1 = headB
            else:
                pt1 = pt1.next
                
            if not pt2:
                pt2 = headA
            else:
                pt2 = pt2.next
                
        return pt1
        
            