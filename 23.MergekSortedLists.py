# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        
        if len(lists) == 0:
            return None
        
        def dfs(lists, l, r):
            if l == r:
                return lists[l]
            
            mid = l + (r - l)//2
            
            left = dfs(lists, l, mid)
            right = dfs(lists, mid+1, r)
            
            return self.mergelist(left, right)
            
        return dfs(lists, 0, len(lists) - 1)
    
    def mergelist(self, l1, l2):
        
        dummy = ListNode(0)
        
        pre = dummy
        
        while l1 and l2:
            
            if l1.val <= l2.val:
                pre.next = l1
                l1 = l1.next
                
            else:
                pre.next = l2
                l2 = l2.next
                
            pre = pre.next
        
        if l1:
            pre.next = l1
        else:
            pre.next = l2
        
        return dummy.next
        
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        
        
        def __lt__(self, other):
            
            return self.val < other.val
        ListNode.__lt__ = __lt__
        
        
        dummy = cur = ListNode()
        
        heap = []
        
        for l in lists:
            if l:
                heapq.heappush(heap, (l.val, l))
        
        while heap:
            
            val, node = heapq.heappop(heap)
            cur.next = ListNode(val)
            cur = cur.next
            if node.next:
                heapq.heappush(heap, (node.next.val, node.next))
        
        return dummy.next
        # amount = len(lists)
        # interval = 1
        # while interval < amount:
        #     for i in range(0, amount - interval, interval * 2):
        #         lists[i] = self.merge2Lists(lists[i], lists[i + interval])
        #     interval *= 2
        # return lists[0] if amount > 0 else None