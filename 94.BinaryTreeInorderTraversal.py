# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    "Recursion version"
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []    
        return self.inorderTraversal(root.left) + [root.val] + self.inorderTraversal(root.right)


class Solution:
    "Iterative version"
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []
        result = []
        stack = [root] 
        while stack:       
            while root.left:
                root = root.left
                stack.append(root)    
            cur = stack.pop()          # be careful here, the cur and root are linked to the same node, so dont change the cur 
            result.append(cur.val)    
            if cur.right:
                root = cur.right
                stack.append(root)  
        return result
            
            
            
        