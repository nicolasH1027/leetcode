# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rangeSumBST(self, root: Optional[TreeNode], low: int, high: int) -> int:
        
        self.total = 0
        def dfs(root, lo, hi):
            if not root:
                return
            
            if lo <= root.val <= hi:
                self.total += root.val
                dfs(root.right, lo, hi)
                dfs(root.left, lo, hi)
            
            if root.val < lo:
                dfs(root.right, lo, hi)
            
            if root.val > hi:
                dfs(root.left, lo, hi)
                
            return 

        dfs(root, low, high)
        
        return self.total


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rangeSumBST(self, root: Optional[TreeNode], low: int, high: int) -> int:
        
        self.total = 0
        def dfs(root, lo, hi):
            if not root:
                return
            
            if lo <= root.val <= hi:
                self.total += root.val

            if root.val > lo:
                dfs(root.left, lo, hi)
            
            if root.val < hi:
                dfs(root.right, lo, hi)
                
            return 

        dfs(root, low, high)
        
        return self.total
            