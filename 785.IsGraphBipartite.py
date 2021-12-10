class Solution:
    def isBipartite(self, graph: List[List[int]]) -> bool:
        "dfs"
        
        color = {}
        
        def dfs(node, val):
            
            color[node] = val
            
            for nxt in graph[node]:
                if nxt not in color:
                    if not dfs(nxt, 1-val):
                        return False
                else:
                    if color[nxt] == val:
                        return False
            return True
        
        for i in range(len(graph)):
            
            if i in color:continue
                
            if not dfs(i, 0):
                return False
        
        return True


class Solution:
    def isBipartite(self, graph: List[List[int]]) -> bool:
        
        "BFS"
        
        queue = collections.deque()
        color = {}
        
        for i in range(len(graph)):
            
            if i in color: continue
            
            color[i] = 0
            queue.append((i, 0))
            
            while queue:
                
                cur, val = queue.popleft()
                
                for nxt in graph[cur]:
                    if nxt not in color:
                        color[nxt] = 1 - val
                        queue.append((nxt, 1-val))
                    else:
                        if color[nxt] == val:
                            return False
        
        return True
                
        