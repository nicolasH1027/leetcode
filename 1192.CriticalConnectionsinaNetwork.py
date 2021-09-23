class Solution:
    def criticalConnections(self, n: int, connections: List[List[int]]) -> List[List[int]]:
        "TLE, Its O(E^2)"
        parent = [i for i in range(n)]
        rank = [1 for i in range(n)]
        def find(x):
            if x != parent[x]:
                parent[x] = find(parent[x])
            return parent[x]
        
        def union(x, y):
            # remmber the technique here, to count how many component
            px, py = find(x), find(y)
            if px == py: return 0
            if rank[px] < rank[py]:
                parent[px] = py
            elif rank[px] > rank[py]:
                parent[py] = px
            else:
                parent[px] = py
                rank[py] += 1  
            return 1      

        edge_num = len(connections)
        result = []
        for i in range(edge_num):
            count = n
            parent = [i for i in range(n)]
            rank = [1 for i in range(n)]
            for j in range(edge_num):
                if j == i: continue
                first, second = connections[j]
                count -= union(first, second)
            if count > 1:
                result.append(connections[i])
        return result

class Solution:
    def criticalConnections(self, n: int, connections: List[List[int]]) -> List[List[int]]:
        """
        DFS
        """
        
        # we first convert the link list into adjacency list
        # and initialize the link dict of all distinct link
        # and initialize the rank array 
        adjList = collections.defaultdict(list)
        conlink = {}
        for start, end in connections:
            adjList[start].append(end)
            adjList[end].append(start)
            conlink[(min(start, end), max(start, end))] = 1
        rank = [None]*n
        
        def dfs(node, depth):
            if rank[node]:              # if the rank exists, that means we already visit the node
                return rank[node]
            rank[node] = depth          # set the rank of current node as depth
            minrank = depth             # minrank is used to keep track of the min rank in the cycle
            for neigh in adjList[node]:
                if rank[neigh] and rank[neigh] == depth - 1: continue       # we dont traverse the parent node
                nextrank = dfs(neigh, depth + 1)
                if nextrank <= depth:                                       # we found cycle, delete the link one by one
                    del conlink[(min(node, neigh), max(node, neigh))]
                minrank = min(nextrank, minrank)                            # keep track of the minimum rank in the cycle
            return minrank
        dfs(0, 0)
        result = []
        for i, j in conlink:
            result.append([i, j])
        return result
                
                
                