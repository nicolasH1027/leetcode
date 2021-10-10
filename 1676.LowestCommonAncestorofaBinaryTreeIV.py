# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', nodes: 'List[TreeNode]') -> 'TreeNode':
        if len(nodes) == 1:
            return nodes[0]
        
        def dfs(root, p, q):
            if not root:
                return None
            
            if root == p or root == q:
                return root
            
            left = dfs(root.left, p, q)
            right = dfs(root.right, p, q)
            
            if left and right:
                return root
            
            return left or right
        
        p = nodes[0]
        for i in range(1, len(nodes)):
            p = dfs(root, p, nodes[i])
        
        return p

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', nodes: 'List[TreeNode]') -> 'TreeNode':
        
        def dfs(root):
            
            if not root or root in nodes:
                return root
            
            left = dfs(root.left)
            right = dfs(root.right)
            
            if left and right:
                return root
            
            return left or right
        
        return dfs(root)