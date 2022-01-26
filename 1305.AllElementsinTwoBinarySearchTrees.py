# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def getAllElements(self, root1: TreeNode, root2: TreeNode) -> List[int]:
        
        stack1, stack2 = [], []
        cur1, cur2 = root1, root2
        ans = []
        
        while stack1 or stack2 or cur1 or cur2:
            
            while cur1:
                
                stack1.append(cur1)
                cur1 = cur1.left
            
            while cur2:
                
                stack2.append(cur2)
                cur2 = cur2.left
            
            if not stack2 or stack1 and stack1[-1].val <= stack2[-1].val:
                
                ans.append(stack1[-1].val)
                cur1 = stack1.pop()
                cur1 = cur1.right
            
            else:
                ans.append(stack2[-1].val)
                cur2 = stack2.pop()
                cur2 = cur2.right
                
        return ans