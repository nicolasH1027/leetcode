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