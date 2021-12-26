# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        
        if not root:
            return root
        
        queue = collections.deque([root])
        ans, flag = [], 0
        
        while queue:
            
            n = len(queue)
            flag %= 2
            tmp = collections.deque()
            for _ in range(n):
                node = queue.popleft()
                if flag:
                    tmp.appendleft(node.val)
                else:
                    tmp.append(node.val)
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
     
            ans.append(tmp)
            flag += 1
        
        return ans


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        
        if not root:
            return root
        
        
        ans, level = [], 0
        
        def dfs(node, level):
            
            if level == len(ans):
                ans.append(collections.deque([node.val]))
            else:
                if level % 2:
                    ans[level].appendleft(node.val)
                else:
                    ans[level].append(node.val)         
            for child in [node.left, node.right]:
                if child:
                    dfs(child, level + 1)
                    
        dfs(root, level)
        return ans