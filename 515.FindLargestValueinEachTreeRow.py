# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def largestValues(self, root: Optional[TreeNode]) -> List[int]:
        
        if not root:
            return []
        
        ans = []
        queue = collections.deque()
        queue.append([root, 0])
        
        while queue:
            
            cur, level = queue.popleft()
            
            if level == len(ans):
                ans.append(cur.val)
            else:
                ans[level] = max(ans[level], cur.val)
                
            for child in [cur.left, cur.right]:
                if child:
                    queue.append([child, level + 1])
                    
            
        return ans
        

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def largestValues(self, root: Optional[TreeNode]) -> List[int]:
        
        self.ans = []
        
        def dfs(root, level):
            if not root:
                return 
            
            if level == len(self.ans):
                self.ans.append(root.val)
            else:
                self.ans[level] = max(self.ans[level], root.val)
                
            dfs(root.left, level + 1)
            dfs(root.right, level + 1)
        dfs(root, 0)
        return self.ans