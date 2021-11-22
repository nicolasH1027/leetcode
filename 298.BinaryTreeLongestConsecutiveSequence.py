class Solution:
    def longestConsecutive(self, root: Optional[TreeNode]) -> int:
        "bottom up"
        self.max_len = -float('inf')
        
        def helper(root):
            if not root:
                return None, 0
            
            left, left_length = helper(root.left)
            right, right_length = helper(root.right)
            
            length = 0
            
            if left:
                if left.val - 1 == root.val:
                    length = max(left_length, length)
            if right:
                if right.val - 1 == root.val:
                    length = max(right_length, length)
            
            self.max_len = max(self.max_len, length + 1)
            
            return root, length + 1
        
        helper(root)
                
        return self.max_len

class Solution:
    def longestConsecutive(self, root: Optional[TreeNode]) -> int:
        "Top Down"
        
        def helper(root, parent, length):
            if not root:
                return length
            
            if root and root.val == parent.val + 1:
                path = length + 1
            else:
                path = 1
                
            return max(path, max(helper(root.left, root, path), helper(root.right, root, path)))
        
        return helper(root, None, 0)