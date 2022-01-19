# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def numComponents(self, head: Optional[ListNode], nums: List[int]) -> int:
        
        "straightforward solution without thinking"
        
        graph = collections.defaultdict(list)
        
        for val in nums:
            graph[val] = []
            
        
        while head and head.next:
            
            if head.val in graph and head.next.val in graph:
                
                graph[head.val].append(head.next.val)
                graph[head.next.val].append(head.val)
                
            head = head.next
            
        
        cnt = 0
        seen = set()
        def dfs(node):
            for child in graph[node]:
                if child in seen: continue
                seen.add(child)
                dfs(child)
            
        for key in graph.keys():
            
            if key in seen: continue
                
            seen.add(key)
            
            dfs(key)
            
            cnt += 1
            
        return cnt
    

class Solution:
    def numComponents(self, head: Optional[ListNode], nums: List[int]) -> int:
        
        nodes = set(nums)
        cnt = 0
        
        while head:
            
            if head in nodes and (head.next is None or head.next not in nodes):
                cnt += 1
                
            head = head.next
        
        return cnt
        