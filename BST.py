# search specific node, return null if not exist 
from typing import Counter


class Node:
    def __init__(self, val, left = None, right = None) -> None:
        self.val = val
        self.left = left
        self.right = right


def searchRecursion(root, p):
    "recursion implementation"
    if not root or root.val == p.val:
        return root
    return searchRecursion(root.left, p) if root.val > p.val else searchRecursion(root.right, p)

def searchIterative(root, p):
    while root:
        if root.val < p.val:
            root = root.right
        elif root.val > p.val:
            root = root.left
        else:
            return root
    return root

def InsertIterative(root, p):
    "return root after insertion"
    parent, current = None, root
    
    if not root:
        return p
    
    while current:
        
        if current.val == p.val:
            return root
        elif current.val > p.val:
            parent = current
            current = current.left
        else:
            parent = current
            current = current.right
    
    if parent.val > p.val:
        parent.left = p
    else:
        parent.right = p
    
    return root
    

def InsertRecursion(root, p):
    
    if not root or root.val == p.val:
        return p
    
    if root.val > p.val: 
        root.left = InsertRecursion(root.left, p)
    else:
        root.right = InsertRecursion(root.right, p)
        
    return root

# utilizing the BST property
    
def BSTsuccessor(root, p):
    "successor"
    
    if p.right:   
        leftmost = p.right
        while leftmost.left:
            leftmost = leftmost.left
        return leftmost
    else:
        parent, current  = None, root
        while current:
            if current == p:
                return parent
            elif current.val < p.val:
                current = current.right
            else:
                parent = current
                current = current.left
        
def BSTpredecessor(root, p):
    "predecessor"

    if p.left:
        rightmost = p.left
        while rightmost.right:
            rightmost = rightmost.right
        return  rightmost
    else:
        parent, current = None, root
        while current:
            if current == p:
                return parent
            elif current.val < p.val:
                parent = current
                current = current.right
            else:
                current = current.left


# without utilizing the BST property 

def SuccessorRecursion(root, p):
    
    if p.right:
        leftmost = p.right
        while leftmost.left:
            leftmost = leftmost.left
        return leftmost
    else:
        prev, inordersuccessor = None, None
        inordercase2(root, p)


def inordercase2(root, p):
    
    if not root:
        return
    
    inordercase2(root.left, p)
    
    if prev == p and not inordersuccessor:
        inordersuccessor = root
        return 
    
    prev = root
    
    inordercase2(root.right, p)
    

def SuccessorIterative(root, p):
    
    if p.right:
        leftmost = p.right
        while leftmost.left:
            leftmost = leftmost.left
        return leftmost
    else:
        
        succcessor, current = None, root
        stack = [current]
        prev = False
        while stack:
            while current.left:
                current = current.left
                stack.append(current)
            
            cur = stack.pop()
            if prev: return cur
            if cur == p: prev = True
            if cur.right: 
                current = cur.right
                stack.append(current)
        return succcessor
            
            
        
def PredecessorRecursion(root, p):
    
    
    if p.left:
        rightmost = p.left
        while rightmost:
            rightmost = rightmost.right
        return rightmost
    else:
        
        prev, inorderpredecessor = None, None
        inodercase2pred(root, p)
        return 
        
def inodercase2pred(root, p):
    
    if not root:
        return 

    prev = inodercase2pred(root.left, p)

    if root == p:
        return prev
    
    inodercase2pred(root.right, p)


def PredecessorIterative(root, p):
    
    if p.left:
        rightmost = p.left
        while rightmost.right:
            rightmost = rightmost.right
        return rightmost
    else:
        prev, current = None, root
        stack = [current]
        while stack:
            while current.left:
                current = current.left
                stack.append(current)
            node = stack.pop()
            if node == p: return prev
            prev = node   
            if node.right:
                current = node.right
                stack.append(current)
            
        
            
# delete node in BST 

class Solution:
    "Iterative method"
    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:     
        if not root:
            return None   
        parent, cur = None, root
        while cur and cur.val != key:
            parent = cur
            if cur.val > key:
                cur = cur.left
            else:
                cur = cur.right       
        if not cur:
            return root
        if not cur.left and not cur.right:
            if cur != root:
                if parent.val < key:
                    parent.right = None
                    return root
                else:
                    parent.left = None
                    return root
            else:
                root = None
                return root  
        elif cur.left and cur.right:
            tmp = cur
            rightmost = cur.left
            while rightmost.right:
                tmp = rightmost
                rightmost = rightmost.right
            cur.val = rightmost.val          
            if tmp != cur:
                tmp.right = rightmost.left
            else:
                tmp.left = rightmost.left
            return root
        else:
            if cur.left:
                child = cur.left
            else:
                child = cur.right          
            if cur == root:
                root = child
            else:
                if cur == parent.left:
                    parent.left = child
                else:
                    parent.right = child                   
            return root

class Solution:
    "Recursion method"
    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        
        if not root:
            return None     
        else:
            if root.val == key:
                root = self.delete(root)
            elif root.val < key:
                root.right = self.deleteNode(root.right, key)
            else:
                root.left = self.deleteNode(root.left, key)
        return root
    
    def delete(self, node):
        
        if not node.left:
            return node.right
        elif not node.right:
            return node.left    
        else:
            tmp = node
            rightmost = node.left
            while rightmost.right:
                tmp = rightmost
                rightmost = rightmost.right
            node.val = rightmost.val          
            if tmp != node:
                tmp.right = rightmost.left
            else:
                tmp.left = rightmost.left
            return node