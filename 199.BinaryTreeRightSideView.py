# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        
        """
        O(N) time complexity,  note here that the space complexity is O(N/2) for complete tree
        """
        if not root:
            return []
        
        queue = collections.deque()
        queue.append(root)
        res = []
        
        while queue:
            
            n = len(queue)
            
            for i in range(n):
                cur = queue.popleft()
                if cur.left:
                    queue.append(cur.left)
                if cur.right:
                    queue.append(cur.right)
            res.append(cur.val)
        
        return res
    


class Solution:
    def rightSideView(self, root: TreeNode) -> List[int]:
        """
        O(N) time,  O(H) space, H is logN
        """
        
        if root is None:
            return []
        
        rightside = []
        
        def helper(node: TreeNode, level: int) -> None:
            if level == len(rightside):
                rightside.append(node.val)
            for child in [node.right, node.left]:
                if child:
                    helper(child, level + 1)
                
        helper(root, 0)
        return rightside