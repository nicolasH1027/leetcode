# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def verticalOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        
        """
        Frist idea, BFS traverse the tree, then append the element in res into the final result 
        
        O(3*N)
        """
        
        res = []
        
        queue = collections.deque()
        queue.append((root, 0))
        
        while queue:
            
            cur, level = queue.popleft()
            if cur:
                res.append((cur.val, level))
                queue.append((cur.left, level - 1))
                queue.append((cur.right, level + 1))
        
        lo = inf
        hi = -inf
        for _, level in res:
            lo = min(lo, level)
            hi = max(hi, level)

        verorder = []
        
        for val, level in res:
            pos = level - lo
            while pos > len(verorder) - 1:
                verorder.append([])
            verorder[level - lo].append(val)
        
        return verorder


class Solution:
    def verticalOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        
        """
        Frist idea, BFS traverse the tree, then append the element in res into the final result 

        """
        if not root:
            return []
        res = collections.defaultdict(list)
        queue = collections.deque()
        queue.append((root, 0))
        
        while queue:
            
            cur, level = queue.popleft()
            if cur:
                res[level].append(cur.val)
                queue.append((cur.left, level - 1))
                queue.append((cur.right, level + 1))
        
        lo = inf
        for level in res:
            lo = min(lo, level)
        
        return [res[i] for i in range(lo, lo + len(res))]


