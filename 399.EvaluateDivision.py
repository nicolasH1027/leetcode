class unionfind:
    
    def __init__(self):
        self._weight = {}
        
    def find(self, nodeid):
        
        if nodeid not in self._weight:
            self._weight[nodeid] = (nodeid, 1)
        
        
        stack = [nodeid]
        while stack:
            if stack[-1] != self._weight[stack[-1]][0]:       
                stack.append(self._weight[stack[-1]][0])
            else:
              break
        while stack:
          cur = stack.pop()
          if not stack:
            break
          self._weight[stack[-1]] = (self._weight[cur][0], self._weight[stack[-1]][1] * self._weight[cur][1])

        return self._weight[nodeid]

    
    def union(self, dividend, divisor, value):
        
        dividend_id, dividend_weight = self.find(dividend)
        divisor_id, divisor_weight = self.find(divisor)
        
        if dividend_id != divisor_id:
            self._weight[dividend_id] = (divisor_id, value \
                                         * divisor_weight/dividend_weight)

class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        
        disjoint = unionfind()
        
        for equation, value in zip(equations, values):
            disjoint.union(equation[0], equation[1], value)
         
        result = []
        for (i, j) in queries:
            
            if i not in disjoint._weight or j not in disjoint._weight:
                result.append(-1)
                continue

            hi, hj = disjoint.find(i), disjoint.find(j)
            if hi[0] != hj[0]:
                
                result.append(-1)
                
                continue
            
            result.append(hi[1]/hj[1])
        
        return result