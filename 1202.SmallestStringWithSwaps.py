class Solution:
    def smallestStringWithSwaps(self, s: str, pairs: List[List[int]]) -> str:
        
        parent = [i for i in range(len(s))]
        rank = [1 for i in range(len(s))]
        
        def find(u):
            if u != parent[u]:
                parent[u] = find(parent[u])
            return parent[u]
        
        def union(x, y):
            px, py = find(x), find(y)
            
            if px == py: return
            
            if rank[px] < rank[py]: 
                parent[px] = py
            elif rank[py] < rank[px]: 
                parent[py] = px
            else:
                parent[px] = py
                rank[py] += 1 
            return
        
        cluster = collections.defaultdict(list)
        
        for i, j in pairs:
            union(i, j)
            
        for i in range(len(s)):
            cluster[find(i)].append(s[i])
            
        for key in cluster.keys():
            cluster[key].sort(reverse = True)
        
        res = []
        
        for i in range(len(s)):
            res.append(cluster[find(i)].pop())
        
        return "".join(res)