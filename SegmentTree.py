class TreeNode(object):
    def __init__(self, start, end, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        self.start = start
        self.end = end
        

def build(nums, L, R):
    if L == R:
        return TreeNode(L, R, nums[L])
    
    mid = L + (R - L)//2
    node = TreeNode(L, R)
    node.left = build(nums, L, mid)
    node.right = build(nums, mid + 1, R)
    node.val = node.left.val + node.right.val
    
    return node

def update(nums, root, idx, val):
    if root.start == root.end:
        nums[idx] = val
        root.val = val
        return
    
    mid = root.start + (root.end - root.start) // 2
    if idx <= mid:
        update(nums, root.start, mid, root.left, idx, val)
    else:
        update(nums, mid + 1, root.end, root.right, idx, val)
        
    root.val = root.left.val + root.right.val
    
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
    
    