# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        "Top-Down manner"
        def helper(root, depth):
            if not root:
                return
            self.max_depth = max(self.max_depth, depth+1)
            helper(root.left, depth+1)
            helper(root.right, depth+1)
        self.max_depth = 0
        helper(root, 0)
        return self.max_depth

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        "Bottom-Up manner"
        if not root:
            return 0
        return max(self.maxDepth(root.left), self.maxDepth(root.right)) + 1
    
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        "DFS iterative"
        stack = []
        if root:
            stack.append(root, 1)
        depth = 0
        while stack:
            cur, dep = stack.pop()
            depth = max(depth, dep)
            for node in [cur.left, cur.right]:
                if node:
                    stack.append((node, dep+1))
        return depth

    

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        "BFS recursion, Level order"
        if not root:
            return 0
        def BFS(root, level):
            if level not in cur:
                cur[level] = 1
            for child in [root.left, root.right]:
                if child:
                    BFS(child, level+1)
        cur = {}
        BFS(cur, 0)
        return len(cur)
    

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        "BFS iterative"
        if not root:
            return 0
        
        queue = collections.deque()
        queue.append(root)
        level = 0
        while queue:
            n = len(queue)
            level += 1
            for _ in range(n):
                cur = queue.popleft()
                if cur.left:
                    queue.append(cur.left)
                if cur.right:
                    queue.append(cur.right)
        return level
                
        
        