# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        
        dummy = ListNode()      # use dummy to keep track of the root node of result
        prev = dummy
        carry = 0
        
        while True:
            
            first = 0 if not l1 else l1.val
            second = 0 if not l2 else l2.val
            curval = (first + second + carry) % 10
            carry = 1 if first + second + carry >= 10 else 0
            
            tmp = ListNode(curval)
            prev.next = tmp
            prev = tmp
            
            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None
            
            if not l1 and not l2 and carry == 0:  # don't forget the carry condition here
                break
        return dummy.next
            