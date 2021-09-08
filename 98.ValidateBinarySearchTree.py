# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    "Valid range method. Recursion Version"
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        
        return self.helper(root, -inf, inf)
    
    def helper(self, root, left, right):
        
        if not root:
            return True
        
        if left < root.val < right:
            return self.helper(root.left, left, root.val) and self.helper(root.right, root.val, right)
        else:
            return False
        

class Solution:
    "Valid range method. Iterative Version"
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return True

        stack = [(root, -inf, inf)]
        
        while stack:
            cur, left, right = stack.pop()
            if not cur:
                continue
            elif left < cur.val < right:
                stack.append((cur.left, left,cur.val))
                stack.append((cur.right, cur.val, right))
            else:
                return False
        
        return True
                
            
class Solution:
    "Inorder Traversal. Recursion Version"
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        self.prev = -inf

        return self.helper(root)
    
    def helper(self, root):
        
        if not root:
            return True
        
        left = self.helper(root.left)
        
        if not left or self.prev >= root.val:
            return False
        
        self.prev = root.val

        return self.helper(root.right)
        
class Solution:
    "Inorder Traversal. Iterative Version"
    def isValidBST(self, root: Optional[TreeNode]) -> bool: 
        if not root:
            return True   
        prev = -inf
        stack = [root]   
        while stack:
            while root.left:
                root = root.left
                stack.append(root)
            cur = stack.pop()
            if prev >= cur.val:
                return False
            prev = cur.val
            if cur.right:
                root = cur.right
                stack.append(root)
        return True
            
                
        
        
        
        
        
        