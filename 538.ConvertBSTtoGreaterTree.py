# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def convertBST(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        
        self.sum = 0
        def dfs(root):
            if not root:
                return 
            
            dfs(root.right)     
            self.sum += root.val
            root.val = self.sum
            dfs(root.left)

        dfs(root)
        
        return root
    

class Solution:
    def convertBST(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        
        pathSum = 0
        cur, stack = root, []
        
        while cur or stack:
            if cur:
                stack.append(cur)
                cur = cur.right
            else:
                cur = stack.pop()
                pathSum += cur.val
                cur.val = pathSum
                cur = cur.left
        return root
            