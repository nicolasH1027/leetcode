import collections


class Solution:
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:
        
        """
        Union-Find method
        
        O(Sum(A_ilogA_i)),
        """
        
        parent = [i for i in range(10001)]
        rank = [1 for i in range(10001)]
        
        def find(x):
            if x != parent[x]:
                parent[x] = find(parent[x])
            return parent[x]
        
        def union(x, y):
            px, py = find(x), find(y)
            if px == py: return
            if rank[px] > rank[py]:
                parent[py] = px
            elif rank[px] < rank[py]:
                parent[px] = py
            else:
                parent[py] = px
                rank[px] += 1
            return 
        
        email_name = {}
        email_id = {}
        i = 0
        
        for acc in accounts:
            
            name = acc[0]
            
            for email in acc[1:]:
                email_name[email] = name
                if email not in email_id:
                    email_id[email] = i
                    i += 1
                union(email_id[acc[1]], email_id[email])
        
        ans = collections.defaultdict(list)
        
        for email in email_name:
            ans[find(email_id[email])].append(email)
        
        return [[email_name[v[0]]] + sorted(v) for v in ans.values()]
                
            
            
class Solution(object):
    def accountsMerge(self, accounts):
        
        """
        DFS, same complexity with disjoint set (with rank and path compression)
        
        The idea is to build a graph and make all those emails with the same person connected
        """
        
        graph = collections.defaultdict(set)
        names = {}
        res = []
        
        for acc in accounts:
            name = acc[0]
            for email in acc[1:]:
                graph[acc[1]].add(email)
                graph[email].add(acc[1])
                names[email] = name
        
        seen = set()
        for node in graph:
            if node in seen: continue
            seen.add(node)
            stack = [node]
            comp = []
            while stack:
                cur = stack.pop()
                comp.append(cur)
                for child in graph[cur]:
                    if child in seen: continue
                    stack.append(child)
                    seen.add(child)
            res.append([names[node]] + sorted(comp))
        
        return res
        
            
            
            
            
            
            
            
        
        
            