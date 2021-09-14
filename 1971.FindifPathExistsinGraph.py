from typing import List


class UnionFindSet:
    def __init__(self, n):
        self._parents = [i for i in range(n)]
        self._ranks = [1 for i in range(n)]
    
    def find(self, u):
        stack = [u]

        while stack:
          cur = stack.pop()
          if cur != self._parents[cur]:
            stack.append(self._parents[cur])
  
        while u != self._parents[u]:
          tmp = self._parents[u]
          self._parents[u] = cur
          u = tmp

        return cur
  
    def union(self, u, v):
        pu, pv = self.find(u), self.find(v)
        if pu == pv: return False
        
        if self._ranks[pu] < self._ranks[pv]:
            self._parents[pu] = pv
        elif self._ranks[pu] > self._ranks[pv]:
            self._parents[pv] = pu
        else:        
            self._parents[pv] = pu
            self._ranks[pu] += 1
        
        return True

class Solution:
    def validPath(self, n: int, edges: List[List[int]], start: int, end: int) -> bool:
        "time complexity O(v)"
        disjoinset = UnionFindSet(n)
        for i, j in edges:
            disjoinset.union(i, j)
        
        return disjoinset.find(start) == disjoinset.find(end)

class Solution:
    def validPath(self, n: int, edges: List[List[int]], start: int, end: int) -> bool:
        "Disjoint Set simplified version but not as efficient as original one"
        
        parent =  [i for i in range(n)]
        
        def find(x):
            while x != parent[x]: 
                x = parent[x] 
            return parent[x]
        
        def union(x, y):
            x_root = find(x)
            y_root = find(y)
            if x_root != y_root:
                parent[y_root] = x_root

        for i, j in edges:
            union(i, j)
            
        return find(start) == find(end)

class Solution:
    def validPath(self, n: int, edges: List[List[int]], start: int, end: int) -> bool:
        "DFS"
        
        adjList = collections.defaultdict(list)
        for i, j in edges:
            adjList[i].append(j)
            adjList[j].append(i)
        seen = set()
        seen.add(start)
        stack = []
        stack.append(start)
        
        while stack:
            cur = stack.pop()
            if cur == end: return True
            for node in adjList[cur]:
                if node in seen: continue
                seen.add(node)
                stack.append(node)
        return False 

class Solution:
    def validPath(self, n: int, edges: List[List[int]], start: int, end: int) -> bool:
        "DFS, call stack Version"
        adjList = collections.defaultdict(list)
        for i, j in edges:
            adjList[i].append(j)
            adjList[j].append(i)
        seen = set()
        seen.add(start)
        
        def dfs(node, end, seen, adjList):
            if node  == end: return True

            for nei in adjList[node]:
                if nei in seen: continue
                seen.add(nei)
                if dfs(nei, end, seen, adjList):
                    return True
            return False   
        return dfs(start, end, seen, adjList) 
    




class Solution:
    def validPath(self, n: int, edges: List[List[int]], start: int, end: int) -> bool:
        "BFS"
        
        adjList = collections.defaultdict(list)
        for i, j in edges:
            adjList[i].append(j)
            adjList[j].append(i)
        seen = set()
        seen.add(start)
        queue = collections.deque()
        queue.append(start)
        
        while queue:
            cur = queue.popleft()
            if cur == end: return True
            for node in adjList[cur]:
                if node in seen: continue
                seen.add(node)
                queue.append(node)
        return False   