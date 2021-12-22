# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        if not root and not subRoot:
            return True
        
        if not root or not subRoot:
            return False
        
        if root.val == subRoot.val and self.compare(root, subRoot):
            print(root.val)
            return True
        
        return self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot)
        
    
    def compare(self, s, t):
        
        if not s and not t:
            return True
        
        if not s or not t:
            return False
        
        if s.val != t.val:
            return False
        
        if s.val == t.val:
            return self.compare(s.left, t.left) and self.compare(s.right, t.right)
        

class Solution:
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        "KMP"
        
        
def getnext(s):
    m = len(s)
    next_ind = [0]*m
    k = 0
    for i in range(1, m):
        while k > 0 and s[k] != s[i]:
            k = next_ind[k-1]

        if s[k] == s[i]:
            k += 1

    next_ind[i] = k
  
    return next_ind
  
def kmp(s, t):
    n, m = len(s), len(t)
    next_ind = [0, 0, 0, 0, 4, 0]
    q = 0

    for i in range(n):
        while q > 0 and t[q] != s[i]:
            q = next_ind[q-1]

        if t[q] == s[i]:
            q += 1

        if q == m:
            print('found')
            print(i - m + 1)
            q = next_ind[q-1]