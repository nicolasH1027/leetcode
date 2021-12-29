# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rob(self, root: Optional[TreeNode]) -> int:
        
        @lru_cache(None)
        def helper(root):
            
            if not root:
                return 0
            ans = root.val
            if root.left:
                ans += helper(root.left.left)+helper(root.left.right)

            if root.right:
                ans += helper(root.right.left) + helper(root.right.right)

            return max(ans, helper(root.left) + helper(root.right))
        
        return helper(root)


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rob(self, root: Optional[TreeNode]) -> int:
        
        def helper(root):
            if not root:
                return [0, 0]
            
            left = helper(root.left)
            right = helper(root.right)
            
            ans = [0, 0]
            
            ans[0] = root.val + left[1] + right[1]
            ans[1] = max(left) + max(right)
            
            return ans
        
        return max(helper(root))