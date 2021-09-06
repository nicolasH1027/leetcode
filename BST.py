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
            
        
            
        