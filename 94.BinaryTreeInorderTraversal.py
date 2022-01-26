# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    "Recursion version, not efficient way"
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []    
        return self.inorderTraversal(root.left) + [root.val] + self.inorderTraversal(root.right)
    
class Solution:
    "Recursion version, efficient way"
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        
        def helper(root):
            if not root:
                return
            helper(root.left)
            result.append(root.val)
            helper(root.right)            
        result = []
        helper(root)
        return result
    


class Solution:
    "Iterative version, consistent with Template"
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        stack = []
        result = []
        cur = root
        while stack or cur:
            
            if cur:
                stack.append(cur)
                cur = cur.left
            else:
                cur = stack.pop()
                result.append(cur.val)
                cur = cur.right
        return result


class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        "Morris traversal O(1) memory complexity"

    
    
    
    
class Solution:
    "Iterative version, not consistent with Template"
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []
        result = []
        stack = [root] 
        while stack:       
            while root.left:
                root = root.left
                stack.append(root)    
            cur = stack.pop()          # be careful here, the cur and root are linked to the same node, if we change the left of cur now, then it will fail to infinite loop
            result.append(cur.val)    
            if cur.right:
                root = cur.right
                stack.append(root)  
        return result
            
            
            
        