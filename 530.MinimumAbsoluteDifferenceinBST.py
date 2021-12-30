# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def getMinimumDifference(self, root: Optional[TreeNode]) -> int:
        
        prev, stack, cur, ans = None, [], root, float('inf')
        
        while stack or cur:
            
            if cur:
                stack.append(cur)
                cur = cur.left
            else:
                cur = stack.pop()
                if prev is not None:
                    ans = min(ans, abs(cur.val - prev))
                prev = cur.val
                cur = cur.right
            
        return ans        