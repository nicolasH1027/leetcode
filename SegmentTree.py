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
    


"""
implementation with another array
"""

tree = [0]*(4*len(nums))

def build(nums, tree, node, start, end):
    if start == end:
        tree[node] = nums[start]
        return
    
    mid = start + (end - start) // 2
    leftnode = 2*node + 1
    rightnode = 2*node + 2
    
    build(nums, tree, leftnode, start, mid)
    build(nums, tree, rightnode, mid + 1, end)
    tree[node] = tree[leftnode] + tree[rightnode]
    
    
def update(nums, tree, node, start, end, idx, val):
    if start == end:
        nums[idx] = val
        tree[node] = val
        return
    
    mid = start + (end - start) // 2
    left = 2*node + 1
    right = 2*node + 2
    if idx <= mid:
        update(nums, tree, left, start, mid, idx, val)
    else:
        update(nums, tree, right, mid + 1, end, idx, val)
    
    tree[node] = tree[left] + tree[right]

def query(tree, node, start, end,  L, R):
    if start == end:
        return tree[node]
    
    if start == L and end == R:
        return tree[node]
    
    mid = start + (end - start)//2
    left = 2*node + 1
    right = 2*node + 2
    
    if R <= mid:
        return query(tree, left, start, mid, L, R)
    elif L > mid:
        return query(tree, right,  mid+1, end, L, R)
    else:
        leftsum = query(tree, left, start, mid, L, R)
        rightsum = query(tree, right, mid+1, end, L, R)
        return leftsum + rightsum