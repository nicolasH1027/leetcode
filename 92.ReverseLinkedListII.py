# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        "Iterative"
        "two pointer, same with 206"
        dummy = ListNode()
        dummy.next = head
        
        lpt = dummy
        
        while left > 1:
            lpt = lpt.next
            left -= 1
            right -= 1
            
        newhead = None
        cur = lpt.next
        rev_tail = lpt. next
        
        while right:
            
            tmp = cur.next
            cur.next = newhead
            newhead = cur
            cur = tmp
            right -= 1
        
        lpt.next = newhead
        rev_tail.next = tmp
        return dummy.next 
    
class Solution:
    "recursion"
    
    def __init__(self) -> None:
        
        self.successor = None
    
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        if left == 1:
            return self.reverse(head, right)
        
        head.next = self.reverseBetween(head.next, left - 1, right)
        
        return head

    
    def reverse(self, head, n):
        if n == 1:
            self.successor = head.next
            return head
        
        last = reverse(head.next, n - 1)
        
        head.next.next = head
        head.next = self.successor
        
        return last    

class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        """
        Recursion method, instead of reversing, swap the value
        """

        if not head:
            return None

        left, right = head, head
        stop = False
        def recurseAndReverse(right, m, n):
            nonlocal left, stop

            # base case. Don't proceed any further
            if n == 1:
                return

            # Keep moving the right pointer one step forward until (n == 1)
            right = right.next

            # Keep moving left pointer to the right until we reach the proper node
            # from where the reversal is to start.
            if m > 1:
                left = left.next

            # Recurse with m and n reduced.
            recurseAndReverse(right, m - 1, n - 1)

            # In case both the pointers cross each other or become equal, we
            # stop i.e. don't swap data any further. We are done reversing at this
            # point.
            if left == right or right.next == left:
                stop = True

            # Until the boolean stop is false, swap data between the two pointers     
            if not stop:
                left.val, right.val = right.val, left.val

                # Move left one step to the right.
                # The right pointer moves one step back via backtracking.
                left = left.next           

        recurseAndReverse(right, left, right)
        return head
        