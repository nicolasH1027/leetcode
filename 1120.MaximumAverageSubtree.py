# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def maximumAverageSubtree(self, root):
        """
        :type root: TreeNode
        :rtype: float
        """
        
        self.maxavg = -float('inf')
        
        def dfs(root):
            
            if not root:
                return 0., 0
            
            left, n1 = dfs(root.left)
            right, n2 = dfs(root.right)

            avg = (left + root.val + right)/(n1 + n2 + 1)
            
            self.maxavg = max(self.maxavg, avg)
            
            return left + root.val + right, n1 + n2 + 1
        
        dfs(root)
        
        return self.maxavg