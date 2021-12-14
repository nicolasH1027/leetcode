# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string.
        
        :type root: TreeNode
        :rtype: str
        """     
        ans = []   
        def preorder(root):
            if not root:
                ans.append('None')
                return
            
            ans.append(str(root.val))
            preorder(root.left)
            preorder(root.right)
        preorder(root)
        return ','.join(ans)

    def deserialize(self, data):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """
        
        data = data.split(',')
        self.ind = 0
        
        def build(arr):
            
            if arr[self.ind] == 'None':
                self.ind += 1
                return None      
            root = TreeNode(arr[self.ind])
            self.ind += 1  
            root.left = build(arr)
            root.right = build(arr)
            return root
        
        root = build(data)
        
        return root

# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# ans = deser.deserialize(ser.serialize(root))



class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string.
        
        :type root: TreeNode
        :rtype: str
        """     
        ans = []
        def postorder(root):
            if not root:
                ans.append('None')
                return 
            postorder(root.left)
            postorder(root.right)
            ans.append(str(root.val))
            
        postorder(root)
        return ','.join(ans)
            

    def deserialize(self, data):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """
        
        data = data.split(',')
        self.ind = len(data) - 1
        
        def postorder(data):
            
            if data[self.ind] == 'None':
                self.ind -= 1
                return None
            
            root = TreeNode(int(data[self.ind]))
            self.ind -= 1
            
            root.right = postorder(data)
            root.left = postorder(data)
            return root
        
        return postorder(data)            


class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string.
        
        :type root: TreeNode
        :rtype: str
        """     
        if not root:
            return ''
        
        queue = collections.deque()
        queue.append(root)
        ans = []
        
        while queue:
            
            cur = queue.popleft()
            
            if cur:
                ans.append(str(cur.val))
            else:
                ans.append('None')
            
            if cur:
                queue.append(cur.left)
                queue.append(cur.right)
        
        return ','.join(ans)
                    

    def deserialize(self, data):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """
        if not data:
            return None
        
        data = data.split(',')
        queue = collections.deque()
        root = TreeNode(int(data[0]))
        queue.append(root)
        ind, n = 1, len(data)
        
        while ind < n and queue:
            
            node = queue.popleft()
            
            if data[ind] != 'None':
                node.left = TreeNode(int(data[ind]))
                queue.append(node.left)
                
            ind += 1
            
            if data[ind] != 'None':
                node.right = TreeNode(int(data[ind]))
                queue.append(node.right)
            ind += 1
        
        return root
        
        