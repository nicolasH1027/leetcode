# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findDuplicateSubtrees(self, root: Optional[TreeNode]) -> List[Optional[TreeNode]]:
        
        dic = {}
        ans = []
        
        def postorder(root):
            
            if not root:
                return '#'
            
            left = postorder(root.left)
            right = postorder(root.right)
            path = str(root.val) + ','+ left + ',' + right
            
            if dic.get(path, 0) == 1:
                ans.append(root)
                dic[path] = dic.get(path, 0) + 1
            else:
                dic[path] = 1
            
            return path
        
        postorder(root)
        
        return ans
        
        