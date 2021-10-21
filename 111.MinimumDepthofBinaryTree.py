# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution(object):
    def minDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        
        def dfs(root):
            if not root:
                return 0
            
            if not root.left and not root.right:
                return 1
            
            depth = float('inf')
            
            for child in [root.left, root.right]:
                if child:
                    depth = min(depth, dfs(child))

            
            return depth + 1
    
        
        return dfs(root)
    

class Solution(object):
    def minDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        
        "BFS"
        if not root:
            return 0
        queue = collections.deque()
        queue.append((root, 1))
        
        while queue:
            node, level = queue.popleft()
            
            if not node.left and not node.right:
                return level
            
            for child in [node.left, node.right]:
                if child:
                    queue.append((child, level + 1))
        
        
                
                    
        
        