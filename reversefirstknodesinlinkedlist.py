# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

successor = None
def reverseN(head: ListNode, n: int):
    if n == 1:
        successor = head.next
        return head
    
    last = reverseN(head.next, n - 1)
    
    head.next.next = head
    head.next = successor
    return last
    