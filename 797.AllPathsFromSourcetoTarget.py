class Solution:
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        "Naive Backtracking or DFS"
        def DFS(graph, node, track):
            if node == len(graph) - 1:
                result.append(track[:])
                return 
                
            for nei in graph[node]:
                
                track.append(nei)
                DFS(graph, nei, track)
                track.pop()
        result = []
        DFS(graph, 0, [0])
        return result