# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        
        cur, stack = root, []
        
        while cur or stack:
            if cur:
                stack.append(cur)
                cur = cur.left
            else:
                cur = stack.pop()
                k -= 1
                if not k:
                    return cur.val
                stack.append(cur)


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, lcount = 0, left=None, right=None):
        self.val = val
        self.lcount = lcount
        self.left = left
        self.right = right

def insert(root, val):
    if not root:
        return TreeNode(val)
    
    if val < root.val:
        root.left = insert(root.left, val)
        root.lcount += 1
    else:
        root.right = insert(root.right, val)
    
    return root
    
def kthSmallest(root, k):
    
    if not root:
        return root
    
    cnt = root.lcount + 1
    
    if cnt == k:
        return root
    
    if cnt < k:
        return kthSmallest(root.right, k - cnt)
    else:
        return kthSmallest(root.left, k)
    
# [10,5,18,4,8,null,19,null,null,7]