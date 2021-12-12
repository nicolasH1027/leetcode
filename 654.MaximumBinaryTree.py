# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def constructMaximumBinaryTree(self, nums: List[int]) -> Optional[TreeNode]:
        "naive way"
        
        if not nums:
            return None
        
        val = max(nums)
        ind = nums.index(val)
        root = TreeNode(val)
        
        left = self.constructMaximumBinaryTree(nums[:ind])
        right = self.constructMaximumBinaryTree(nums[ind+1:])
        root.left = left
        root.right = right  
        
        return root
    

class Solution:
    def constructMaximumBinaryTree(self, nums: List[int]) -> Optional[TreeNode]:
        
        "巧用单调栈，怒解最大树"
        
        """
        在此问题中，每一次我们要找到数组中的最大值，然后把数组分成两半，左边的数组构成左子树
        右边的数组构成右子树。类似于构造单调递增栈， 遇到比栈顶大的数， 设为cur，就弹出栈顶的元素， 并嫁接
        到cur的左侧，然后跳出循环，如果栈里还有元素，那说明此元素比cur大，那么将cur嫁接到栈顶元素的右侧，因为
        在原数组中，此栈顶元素必然位于cur的左侧
        """
        
        stack = []
        
        for num in nums:
            
            cur = TreeNode(num)
            
            while stack and stack[-1].val < num:
                cur.left = stack.pop()
            
            if stack:
                stack[-1].right = cur
            
            stack.append(cur)
        
        return stack[0]
            