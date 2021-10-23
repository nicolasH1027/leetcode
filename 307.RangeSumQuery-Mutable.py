
class NumArray(object):
    """
    TLE.........s
    """
    def __init__(self, nums):
        """
        :type nums: List[int]
        """
        self.nums = nums
        self.tree = [0]*(4*len(nums))
        self.build(self.nums, self.tree, 0, 0, len(self.nums) - 1)
        
    def update(self, index, val):
        """
        :type index: int
        :type val: int
        :rtype: None
        """
        def helper(nums, tree, node, start, end, index, val):
            if start == end:
                nums[index] = val
                tree[node] = val
                return
            
            mid = start + (end - start) // 2
            left = 2*node + 1
            right = 2*node + 2
            if index <= mid:
                helper(nums, tree, left, start, mid, index, val)
            else:
                helper(nums, tree, right, mid + 1, end, index, val)         
            tree[node] = tree[left] + tree[right]
        helper(self.nums, self.tree, 0, 0, len(self.nums)-1, index, val)

    def sumRange(self, left, right):
        """
        :type left: int
        :type right: int
        :rtype: int
        """
        def helper(tree, node, start, end, L, R):
            if start == end:
                return tree[node]
            if start == L and end == R:
                return tree[node]
            
            mid = start + (end - start) // 2
            left = 2*node + 1
            right = 2*node + 2
            
            if R <= mid:
                return helper(tree, left, start, mid, L, R)
            elif L > mid:
                return helper(tree, right, mid + 1, end, L, R)
            else:
                return helper(tree, left, start, mid, L, R) + helper(tree, right, mid + 1, end, L, R)
            
        return helper(self.tree, 0, 0, len(self.nums)- 1, left, right)
            
        
        
    def build(self, nums, tree, node, start, end):
        if start == end:
            tree[node] = nums[start]
            return
        
        mid = start + (end - start) // 2
        leftnode = 2*node + 1
        rightnode = 2*node + 2
        self.build(nums, tree, leftnode, start, mid)
        self.build(nums, tree, rightnode, mid + 1, end)
        tree[node] = tree[leftnode] + tree[rightnode]
        

# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# obj.update(index,val)
# param_2 = obj.sumRange(left,right)

class TreeNode(object):
    def __init__(self, start, end, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        self.start = start
        self.end = end

class NumArray(object):
    """
    TLE.........s
    """
    def __init__(self, nums):
        """
        :type nums: List[int]
        """
        self.nums = nums
        self.tree = [0]*(4*len(nums))
        self.root = self.build(nums, 0, len(nums)-1)
        
    def update(self, index, val):
        """
        :type index: int
        :type val: int
        :rtype: None
        """
        def helper(nums, root, idx, val):
            if root.start == root.end:
                nums[idx] = val
                root.val = val
                return
            
            mid = root.start + (root.end - root.start) // 2
            if idx <= mid:
                helper(nums, root.left, idx, val)
            else:
                helper(nums,root.right, idx, val)
                
            root.val = root.left.val + root.right.val
        helper(self.nums, self.root, index, val)

    def sumRange(self, left, right):
        """
        :type left: int
        :type right: int
        :rtype: int
        """
        def query(root, left, right):
            if root.left == root.right:
                return root.val

            if root.start == left and root.end == right:
                return root.val
            
            mid = root.start + (root.end- root.start) // 2
            
            if right <= mid:
                return query(root.left, left, right)
            if left > mid:
                return query(root.right, left, right)
            else:
                return query(root.left, left, mid) + query(root.right, mid + 1, right)
            
        return query(self.root, left, right)
            
        
    def build(self,nums, L, R):
        if L == R:
            return TreeNode(L, R, nums[L])
        
        mid = L + (R - L)//2
        node = TreeNode(L, R)
        node.left = self.build(nums, L, mid)
        node.right = self.build(nums, mid + 1, R)
        node.val = node.left.val + node.right.val
        
        return node
