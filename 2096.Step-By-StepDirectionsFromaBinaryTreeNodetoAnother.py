# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def getDirections(self, root: Optional[TreeNode], startValue: int, destValue: int) -> str:
        
        def LCA(root):
            
            if not root:
                return None
            
            if root.val == startValue or root.val == destValue:
                return root            
            
            left = LCA(root.left)
            right = LCA(root.right)
            
            if left and right:
                return root
            
            return left or right
        
        lca = LCA(root)
        
        queue = collections.deque()
        queue.append((lca, ''))
        
        startpath = ''
        endpath = ''
        
        while queue:
            
            cur, path = queue.popleft()
            
            if cur.val == startValue:
                startpath = path
                
            if cur.val == destValue:
                endpath = path
                
            if startpath and endpath:
                break
            
            for node, direc in [(cur.left, 'L'), (cur.right, 'R')]:
                if node:
                    queue.append((node, path + direc))
                    
        return 'U'*len(startpath)+endpath


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def getDirections(self, root: Optional[TreeNode], startValue: int, destValue: int) -> str:
        

        queue = collections.deque()
        queue.append((root, ''))
        
        startpath = ''
        endpath = ''
        
        while queue:
            
            cur, path = queue.popleft()
            
            if cur.val == startValue:
                startpath = path
                
            if cur.val == destValue:
                endpath = path
                
            if startpath and endpath:
                break
            
            for node, direc in [(cur.left, 'L'), (cur.right, 'R')]:
                if node:
                    queue.append((node, path + direc))

        i = 0
        
        while startpath[i:] and endpath[i:]:
            
            if startpath[i] == endpath[i]:
                i += 1
            else:
                break
        
        return 'U'*len(startpath[i:])+endpath[i:]
        
            