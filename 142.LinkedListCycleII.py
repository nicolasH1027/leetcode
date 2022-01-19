# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def detectCycle(self, head: ListNode) -> ListNode:
        
        slow, fast = head, head
        
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if fast == slow:
                break

        if not fast or not fast.next:
            return None
        
        slow = head
        
        while slow != fast:
            fast = fast.next
            slow = slow.next
        
        return slow 

"""
龟兔赛跑重要公式 （假设有cycle）

第一轮， 兔子的速度是乌龟的两倍。

假设进入cycle前的距离为 F, 相遇点为 a，那么我们可以得到

2(F + a) = F + a + nC

-> F + a = nC, 

C 为cycle的周长


那么第二轮，我们把乌龟放回起始点，并且，兔子的速度调整为1，

假设 乌龟和兔子都走 F 步

那么乌龟将在cycle的起始点（根据定义）

兔子呢  (a + F) % c == (a + nC - a) % C = 0

也是在cycle的起始点，所以，此时乌龟和兔子相遇在起始点
"""