# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        
        self.left = head
        
        def helper(head):
            if not head:
                return True
            
            ans = helper(head.next)
            
            ans = ans and head.val == self.left.val
            
            self.left = self.left.next
            
            return ans
        
        return helper(head)
            