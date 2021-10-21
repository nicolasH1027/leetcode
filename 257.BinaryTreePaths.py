# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def binaryTreePaths(self, root):
        """
        :type root: TreeNode
        :rtype: List[str]
        """
        
        res = []
        
        def backtrack(root, track):

            if not root:
                return
            
            track.append(str(root.val) + '->')
            
            if not root.left and not root.right:
                tmp = "".join(track)
                res.append(tmp[:-2])
                track.pop()
                return 
            
            for child in [root.left, root.right]:
                if child:
                    backtrack(child, track)
            track.pop()
        
        backtrack(root, [])
        
        return res
    



class Solution(object):
    def binaryTreePaths(self, root):
        """
        :type root: TreeNode
        :rtype: List[str]
        """
        
        if not root:
            return []
        
        paths = []
        
        stack = [(root, str(root.val))]
        
        while stack:
            
            node, val = stack.pop()
            
            if not node.left and not node.right:
                paths.append(val)
            
            for child in [node.left, node.right]:
                if child:
                    stack.append((child, val + '->' + str(child.val)))
        
        return paths


class Solution(object):
    def binaryTreePaths(self, root):
        """
        :type root: TreeNode
        :rtype: List[str]
        """