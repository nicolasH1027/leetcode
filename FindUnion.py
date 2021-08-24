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
