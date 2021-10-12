# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def recoverTree(self, root: Optional[TreeNode]) -> None:
        """
        Do not return anything, modify root in-place instead.
        
        1. Inorder Traverse the tree, save the node into list.
        
        2. Traverse the list, swap the two misplaced node.
        """
        
        nums = []
        
        def dfs(root):
            if not root:
                return 
            
            dfs(root.left)
            nums.append(root)
            dfs(root.right)
        
        def swap(ls):
            x = y = None
            for i in range(len(ls) - 1):
                if ls[i+1].val < ls[i].val:
                    y = ls[i + 1]
                    
                    if not x:
                        x = ls[i]
                    else:
                        break
            x.val, y.val = y.val, x. val
            return
        
        dfs(root)
        swap(nums)
        
        return
        
            
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def recoverTree(self, root: Optional[TreeNode]) -> None:
        """
        Do not return anything, modify root in-place instead.
        
        1. One pass traverse
        """
        
        nums = []
        
        def dfs(root):
            if not root:
                return 
            
            dfs(root.left)
            
            
            nums.append(root)
            
            
            
            dfs(root.right)
        

        
        return
        
            
class Solution:
    def recoverTree(self, root: Optional[TreeNode]) -> None:
        """
        Do not return anything, modify root in-place instead.
        
        1. One pass traverse
        """
        
        stack = []
        cur = root
        x = y = prev = None
        while stack or cur:
            while cur:
                stack.append(cur)
                cur = cur.left
            else:
                cur = stack.pop()
                if prev:
                    if prev.val > cur.val:
                        y = cur
                        if not x:
                            x = prev
                        else:
                            break
                prev = cur
                cur = cur.right
        x.val, y.val = y.val, x.val
        return root
    

class Solution:
    def recoverTree(self, root: Optional[TreeNode]) -> None:
        """
        Do not return anything, modify root in-place instead.
        
        1. One pass traverse (Recursion)
        """
        
        x = y = prev = None
        
        def dfs(root):
            if not root:
                return
            
            dfs(root.left)
            nonlocal x, y, prev
            if prev:
                if prev.val > root.val:
                    y = root
                    if not x:
                        x = prev
                    else:
                        return
            prev = root
            dfs(root.right)            
            
        dfs(root)
        x.val, y.val = y.val, x.val
        return 