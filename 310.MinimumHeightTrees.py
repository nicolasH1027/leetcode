class Solution:
    def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:

        if n <= 2:
            return [i for i in range(n)]
        
        tree = collections.defaultdict(set)
    
        for src, tar in edges:
            tree[src].add(tar)
            tree[tar].add(src)
            
        # here we use a queue to store all the leaves nodes
        leaves = []
        
        for i in range(n):
            if len(tree[i]) == 1:
                leaves.append(i)
        
        # then we need to cut the leaves layer by layer 
        while True:
            new_leaves = []
            for leaf in leaves:
                for parent in tree[leaf]:
                    tree[parent].remove(leaf)
                    if len(tree[parent]) == 1:
                       new_leaves.append(parent)
            if not new_leaves:
                return leaves
            leaves = new_leaves[:]
                
                
            