# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def plusOne(self, head: ListNode) -> ListNode:
        stack = []
        cur = head
        while cur:
            stack.append(cur)
            cur = cur.next    
        carry = 1
        while stack: 
            cur = stack.pop()
            if carry == 0: break
            carry, val = divmod(cur.val + carry, 10)     
            cur.val = val
        if carry:
            NewHead = ListNode(val = carry, next = head)
        return NewHead if NewHead else head
    
class Solution:
    def plusOne(self, head: ListNode) -> ListNode:
        
        def reverse(node):
            dummy = ListNode()
            cur = node
            while cur:
                tmp = cur.next
                cur.next = dummy.next
                dummy.next = cur
                cur = tmp
            return dummy.next
        
        def AddOne(node):
            carry = 1
            prev = None
            while node:
                if carry == 0: break
                carry, val = divmod(node.val+carry, 10)
                node.val = val
                prev = node
                node = node.next
            if carry:
                prev.next = ListNode(val = carry)
                
        NewHead = reverse(head)
        AddOne(NewHead)

        return reverse(NewHead)


class Solution:
    def plusOne(self, head: ListNode) -> ListNode:
        
        self.carry = 1
        
        def dfs(head):
            
            if not head:
                return 
            
            dfs(head.next)
            
            if self.carry == 0: return
            
            self.carry, val = divmod(head.val + self.carry, 10)
            head.val = val

        dfs(head)
        
        if self.carry:
            return ListNode(self.carry, head)
        
        return head



class Solution:
    def plusOne(self, head: ListNode) -> ListNode:
        """
        most efficient way
        
        two pointer,  the first one points to the rightmost node that is not 9
        the second one points to the rightmost node
        """
        
        dummy = ListNode(next = head)
        
        NonNine, cur = dummy, head
        
        while cur:
            if cur.val != 9:
                NonNine = cur
            cur = cur.next
        
        NonNine.val = NonNine.val + 1
        NonNine = NonNine.next

        while NonNine:
            NonNine.val = 0
            NonNine = NonNine.next

        return dummy.next if dummy.val == 0 else dummy
            
            
            
                