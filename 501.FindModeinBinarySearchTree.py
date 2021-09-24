# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from PrimKruskal import find


class Solution:
    def findMode(self, root: Optional[TreeNode]) -> List[int]:
        "O(n) space complexity"
        freq = {}
        self.max_mode = 0
        
        def preorder(root):
            if not root:
                return
            
            if root.val not in freq:
                freq[root.val] = 1
            else:
                freq[root.val] += 1
            
            self.max_mode = max(self.max_mode, freq[root.val])
            
            preorder(root.left)
            preorder(root.right)
            
        preorder(root)
        result = []
        for key in freq:
            if freq[key] == self.max_mode:
                result.append(key)
        return result

"For the follow up question that required O(1) constant memory, two pass required"
"1 pass to record the maximum count, 2 pass to record the value that appear maximum count times"

class Solution:
    def findMode(self, root: Optional[TreeNode]) -> List[int]:
        """
        
        """
        def findmod(root):
            if root.val != self.curval:
                self.curval = root.val
                self.count = 0
            self.count +=1
            if self.count > self.maxcount:
                self.modesize = 1
                self.maxcount = self.count
            elif self.count == self.maxcount:
                if self.flag:
                   self.result[self.modesize] = root.val
                self.modesize += 1 
        
        def inorder(root):
            if not root:
                return 
            inorder(root.left)
            findmod(root)
            inorder(root.right) 

        
        self.curval = None
        self.count = 0
        self.maxcount = 0
        self.modesize = 0
        self.flag = False

        inorder(root)
        self.curval = None
        self.count = 0
        self.result = [0]*self.modesize
        self.modesize = 0
        self.flag = True
        inorder(root)
        
        return self.result
                

