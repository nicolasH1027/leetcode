# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        "the list concatenation is not efficient"
        if not root:
            return []
        node =  root.val
        left  = self.preorderTraversal(root.left)
        right  = self.preorderTraversal(root.right)
        return [node] + left + right

class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        "Recursion Version, more efficient way"
        def helper(root):
            if not root:
                return          
            result.append(root.val)
            helper(root.left)
            helper(root.right)
        result = []
        helper(root)
        return result
    

# Template for Preoder, Inorder, Postorder 
class Solution:
    def Traversal(self, root: Optional[TreeNode]) -> List[int]:   
        stack = []
        result = []
        cur = root    
        while stack or cur:  
            if cur:
                do_somthing
            else:
                do_something
        return result


            
class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        "Iterative Version, Template"
        stack = []
        result = []
        cur = root
        while stack or cur:
            if cur:
                result.append(cur.val)
                stack.append(cur)
                cur = cur.left
            else:
                cur = stack.pop()
                cur = cur.right
        return result


class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        "Morris traversal O(1) memory complexity"