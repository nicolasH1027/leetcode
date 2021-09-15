"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution:
    def postorder(self, root: 'Node') -> List[int]:
        if not root:
            return []
        res = []
        for child in root.children:
            res.extend(self.postorder(child))
        res.append(root.val)
        return res
    

class Solution(object):
    def postorder(self, root):
        "Iterative Way but similar with preorder traversal"
        if root is None:
            return []
        stack, output = [root], []
        while stack:
            root = stack.pop()
            output.append(root.val)
            for c in root.children:
                stack.append(c)
        return output[::-1]


class Solution(object):
    def postorder(self, root):
        "Iterative way but in postorder traversal"
        # same with binary tree postorder traversal, we need something to help us to keep track of whether we have visited all of the children node.
        # we use two stack here to keep track the information
        if not root:
            return []
        # each number counts for one node and the magnitude of the number means the next position of childnode we need to visited
        stack, counter, result = [root], [0], []
        while stack:
            while counter[-1] < len(stack[-1].children):
                stack.append(stack[-1].children[counter[-1]])
                counter.append(0)
            cur = stack.pop()
            result.append(cur)
            counter.pop()
            if len(counter) != 0:
                counter[-1] += 1
        return result
            
            
        