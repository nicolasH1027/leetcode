# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next


"""
此题有很多种解法

1.
用deque 存储下整条链表，然后分别左右两边 pop

2.
recursion， 设置一个全局变量存储左边， 然后递归调用右边

3.
通过快慢指针找到中点，然后反转右边链表，然后逐一比对。

"""
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        
        queue = collections.deque()
        
        while head:
            queue.append(head)
            head = head.next
        
        while len(queue) >= 2:
            
            left = queue.popleft()
            right = queue.pop()
            
            if left.val != right.val:
                return False
        
        return True

class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        
        self.left = head
        
        "post-order traverse"
        def dfs(node):
            if not node:
                return True
            
            ans = dfs(node.next)
            
            ans = ans and self.left.val == node.val
            
            self.left = self.left.next
            
            return ans
        
        return dfs(head)


class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        
        slow, fast = head, head
        
        while fast and fast.next:
            
            fast = fast.next.next
            slow = slow.next
        
        slow = slow.next if fast else slow 
        
        NewHead = self.reverse(slow)
        
        while NewHead:
            
            if NewHead.val != head.val:
                return False
            
            NewHead = NewHead.next
            head = head.next
        
        return True
            


    def reverse(self, root):
        
        dummy = ListNode()
        
        cur = root
        
        while cur:
            
            tmp = cur.next
            
            cur.next = dummy.next
            
            dummy.next = cur
            
            cur = tmp
        
        return dummy.next
        
            