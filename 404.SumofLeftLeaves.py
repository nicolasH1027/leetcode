# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumOfLeftLeaves(self, root: Optional[TreeNode]) -> int:
        "Tree Traversal, kinda inorder traversal"
        def helper(root):
            if not root:           # check if its a empty node, if yes, return False
                return False
            if not root.left and not root.right: # check if its the leave node, if yes, return True
                return True
            if helper(root.left):  # check the left node of current node, if its leave node, then add the leave node's value to final result
                self.result += root.left.val
            if helper(root.right): # check the right node of current node, if its leave node, then return False
                return
        self.result = 0
        helper(root)
        return self.result


class Solution:
    def sumOfLeftLeaves(self, root: Optional[TreeNode]) -> int:
        "Iterative method"
        "check each node's left child, if its leave node, then add the value to result"        
        stack = [root]
        result = 0
        def is_levae(node):
            return node is not None and not node.left and not node.right
        
        while stack:
            cur = stack.pop()
            if is_levae(cur.left):
                result += cur.left.val
            if cur.right:
                stack.append(cur.right)
            if cur.left:
                stack.append(cur.left)
        return result

class Solution:
    def sumOfLeftLeaves(self, root: Optional[TreeNode]) -> int:
        "Iterative method"
        "we can use one more flag to keep track of the left leave"        
        stack = [(root, 0)]
        result = 0

        while stack:
            cur, flag = stack.pop()
            if not cur.right and not cur.left:
                if flag:
                    result += cur.val
            else:
                if cur.left:
                    stack.append((cur.left, 1))
                if cur.right:
                    stack.append((cur.right, 0))
        return result