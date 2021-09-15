# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        "recursion version"
        if not root:
            return []
        
        return self.postorderTraversal[root.left] + self.postorderTraversal[root.right] + [root.val]
    
class Solution:
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        "recursion version, without list concatenation"
        def helper(root):
            if not root:
                return
            helper(root.left)
            helper(root.right)
            result.append(root.val)
        result = []
        helper(root)
        return result

class Solution:
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        "Iterative way, consistent with Template"
        stack = []
        result = []
        cur = root
        prev = root              # the prev variable is used keep track of last visted node, because in postorder traversal
                                 # we need to traverse left and right substree firstly
        while stack or cur:
            if cur:
                stack.append(cur)
                cur = cur.left
            else: 
                node = stack[-1]
                if not node.right or node.right == prev:
                    stack.pop()
                    result.append(node.val)
                    prev = node
                else:
                    cur = node.right
        return result
