# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findLeaves(self, root: Optional[TreeNode]) -> List[List[int]]:
        
        def dfs(root):
            """
            O(N), N means the number of nodes
            """
            # reach the leaf 
            if not root:
                return 0
            
            # Travese to leaf 
            leftlevel = dfs(root.left)
            rightlevel = dfs(root.right)
            
            # figure out the level of the current root node, and append it into the corresponding list
            level = max(leftlevel, rightlevel)
            
            # cause the level is the index, so if index equals to lenth, that means we need to increase our leaf list 
            if len(leaf) == level:
                leaf.append([])
            leaf[level].append(root.val)
            root.left, root.right = None, None
            return level + 1
        
        leaf = []
        dfs(root)
        return leaf