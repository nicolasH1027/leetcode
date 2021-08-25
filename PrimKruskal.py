# Prim algorithm.  Node iteration

from collections import defaultdict
from heapq import *

n = 4
edges = [[],[],[]]   # edge list
g = defaultdict(list)

for e in edges:
    g[e[0]].append((e[1], e[2]))
    g[e[1]].append((e[0], e[2]))

heap = []
cost = 0
seen = set()
heappush(heap, (0, 0))

for _ in range(n):
    v, w = heappop(heap)
    if v in seen:
        continue
    seen.add(v)
    cost += w
    
    for node, j in g[v]:
        heappush(heap, (node, j))
print(cost)


# Kruskal algorithm.  Edge iteration

n = 4
edges = [[],[],[]]   # edge list
parent = list(range(n))
costs = 0

def find(x):
    if x != parent(x):
        parent(x) = find(parent(x))
    return parent(x)

for start, end, cost in sorted(edges, key= lambda x: x[2]):
    hs = find(start)
    he = find(end)
    
    if hs == he: continue
    
    parent[hs] = he

    costs += cost
    
print(costs)


# implementation of heap

class heapqueue:
    
    def __init__(self, ls = []) -> None:
        self.data = ls
    
    
    def heappush(self, val):
        
        self.data.append(val)
        if len(self.data) == 1:
            return None
        self.upAdjust()
        
    def upAdjust(self):
        
        child_index = len(self.data) - 1
        parent_index = child_index // 2
        tmp = self.data[child_index]
        
        while child_index > 0 and tmp < self.data[parent_index]:
             
             self.data[child_index] = self.data[parent_index]
             child_index = parent_index
             parent_index //= 2
             
        self.data[child_index] = tmp
    
    def heappop(self):
        
        if len(self.data) == 0:
            print("no element in the heap")
            return None
        
        if len(self.data) == 1:
            return self.data.pop()
        
        head = self.data[0]
        self.data[0] = self.data.pop()
        self.downAdjuct()
        
        return head
    
    def downAdjust(self, parent = 0):
        
        # parent = 0
        tmp = self.data[parent]
        childIndex = 2*parent + 1
        
        while childIndex  < len(self.data):
            
            if childIndex + 1 < len(self.data) and self.data[childIndex + 1] < self.data[childIndex]:
                childIndex += 1
                
            if tmp <= self.data[childIndex]:
                break
            
            self.data[parent] = self.data[childIndex]
            parent = childIndex
            childIndex = 2*childIndex + 1
        
        self.data[parent] = tmp
    
    def heapify(self, ls):
        
        self.data = ls
        nonleafnode = len(ls)//2 - 1 # index
        for i in range(nonleafnode, -1, -1):
            self.downAdjust(i)
        
        
        
        
        
    
        
    
