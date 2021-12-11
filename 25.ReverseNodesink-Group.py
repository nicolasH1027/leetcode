# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        
        "Recursion"
        
        if not head:
            return None
        
        a = b = head
        
        for _ in range(k):
            if not b:
                return head
            b = b.next
        
        newhead = self.reverse(a, b)
        a.next = self.reverseKGroup(b, k)
        
        return newhead

        
    def reverse(self, head, tail):
        
        dummy = ListNode()
        cur = head
        
        while cur != tail:
            tmp = cur.next
            cur.next = dummy.next
            dummy.next = cur
            cur = tmp
        
        return dummy.next
        

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        "iterative"
        
        dummy = jump = ListNode()
        dummy.next = l = r = head
        
        while True:
            count = 0

            while r and count < k:
                r = r.next
                count += 1
            
            if count == k:
                newhead = self.reverse(l, r)
                jump.next, jump, l = newhead, l, r
            else:
                jump.next = l
                return dummy.next
                
                
    def reverse(self, head, tail):
        
        dummy = ListNode()
        cur = head
        
        while cur != tail:
            tmp = cur.next
            cur.next = dummy.next
            dummy.next = cur
            cur = tmp
        
        return dummy.next
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        

# # Definition for singly-linked list.
# # class ListNode:
# #     def __init__(self, val=0, next=None):
# #         self.val = val
# #         self.next = next
# class Solution:
#     def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
#         def reversek(head, k):
            
#             if not head:
#                 return head
            
#             cur = head
#             dummy = ListNode()
            
#             while cur and k:
#                 tmp = cur.next
#                 cur.next = dummy.next
#                 dummy.next = cur
#                 cur = tmp
#                 k -= 1
#             head.next = cur
#             return dummy.next, head, cur
        
#         dummy = ListNode(next = head)
#         oldhead, oldtail = dummy, None
        
#         while oldhead.next:
            
#             nhead, ntail, nxt = reversek(oldhead.next, k)
#             oldhead.next = nhead
#             oldhead = ListNode(next = nxt)
#             if oldtail:
#                 oldtail.next = nhead
#             oldtail = ntail
        
#         return dummy.next
            
        