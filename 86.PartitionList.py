# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
        
        Small = SmallHead = ListNode()
        Big = BigHead = ListNode()
        
        while head:
            
            if head.val < x:
                
                Small.next = head
                
                Small = Small.next
            
            else:
                
                Big.next = head
                
                Big = Big.next
            
            head = head.next
            
        
        Big.next = None
        
        Small.next = BigHead.next

        return SmallHead.next