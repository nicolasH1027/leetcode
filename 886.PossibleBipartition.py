class Solution:
    def possibleBipartition(self, n: int, dislikes: List[List[int]]) -> bool:
        
        "dfs"
        
        graph = collections.defaultdict(set)
        
        for src, tar in dislikes:
            graph[src].add(tar)
            graph[tar].add(src)
            
        color = {}
        
        def dfs(root, val):
            
            color[root] = val
            
            for nxt in graph[root]:
                if nxt not in color:
                    if not dfs(nxt, 1-val):
                        return False
                else:
                    if color[nxt] == val:
                        return False
            return True
        
        for key in graph.keys():
            if key in color: continue
            
            if not dfs(key, 0):
                return False
        
        return True
                
            
class Solution:
    def possibleBipartition(self, n: int, dislikes: List[List[int]]) -> bool:
        
        "BFS"
        
        if not dislikes:
            return True

        graph = collections.defaultdict(set)
        
        for src, tar in dislikes:
            graph[src].add(tar)
            graph[tar].add(src)
            
        color = {}
        
        queue = collections.deque()
        
        for key in graph.keys():
            if key in color: continue
            
            color[key] = 0
            queue.append((key, 0))
            
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
                
                        