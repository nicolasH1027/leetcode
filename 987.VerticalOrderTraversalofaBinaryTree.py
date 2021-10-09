# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def verticalTraversal(self, root: Optional[TreeNode]) -> List[List[int]]:

        
        res = collections.defaultdict(list)
        
        def dfs(root, col, row):
            if not root:
                return
            res[col].append((row, root.val))
            dfs(root.left, col - 1, row + 1)
            dfs(root.right, col + 1, row + 1)     
        dfs(root, 0, 0)
        
        lo = inf
        for level in res:
            lo = min(lo, level)
        
        
        return [[val for row, val in sorted(res[x])] for x in range(lo, lo + len(res))]