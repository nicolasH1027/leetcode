"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, next=None):
        self.val = val
        self.next = next
"""

class Solution:
    def insert(self, head: 'Node', insertVal: int) -> 'Node':
        
        newnode = Node(insertVal)
        
        if not head:
            newnode.next = newnode
            return newnode
        
        node = head
        
        while True:
            if node.val <= insertVal <= node.next.val:
                break
            
            if node.val > node.next.val:
                if insertVal >= node.val:
                    break
                elif insertVal <= node.next.val:
                    break
                
            node = node.next
            if node == head:
                break

        newnode.next = node.next
        node.next = newnode
        return head
                