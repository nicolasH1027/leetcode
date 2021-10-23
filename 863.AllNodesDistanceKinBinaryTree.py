# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def distanceK(self, root, target, k):
        """
        :type root: TreeNode
        :type target: TreeNode
        :type k: int
        :rtype: List[int]
        """
        graph = collections.defaultdict(list)
        def buildgraph(root):
            
            for child in [root.left, root.right]:
                if child:
                    graph[root.val].append(child.val)
                    graph[child.val].append(root.val)
                    buildgraph(child)
                    
        buildgraph(root)
        
        res = []
        seen = set()
        def bfs(root, level):
            
            if level == k:
                res.append(root)
                return
            seen.add(root)
            for node in graph[root]:
                if node not in seen:
                    bfs(node, level + 1)
                
        bfs(target.val, 0)
        return res 

# ===================================================
        
        
        
            