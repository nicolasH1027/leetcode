# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
        "Recursion, O(all node)"
        result = []
        def dfs(root, target, track):
            if not root:                # termination condition
                return

            track.append(root.val)      # add the node to the path
            
            if not root.left and not root.right and root.val == target:
                result.append(track[:])
                track.pop()             # small prune, then no need to explore the empyt node
                return
            
            if root.left:
                dfs(root.left, target - root.val, track)
            if root.right:
                dfs(root.right, target - root.val, track)
            track.pop()
        
        dfs(root, targetSum)
        return result