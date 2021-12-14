# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def generateTrees(self, n: int) -> List[Optional[TreeNode]]:
        
        def dfs(l, r):
            if l > r:
                return [None]

            all_root = []
            for i in range(l, r+1):
                left = dfs(l, i-1)
                right = dfs(i+1, r)
                
                for lt in left:
                    for rt in right:
                        root = TreeNode(i)
                        root.left = lt
                        root.right = rt
                        all_root.append(root)
            return all_root
    
        return dfs(1, n) if n else []
            