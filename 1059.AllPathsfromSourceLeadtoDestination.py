class Solution:
    def leadsToDestination(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        "Simple backtracking or DFS"
        adjList = collections.defaultdict(list)
        for i, j in edges:
            adjList[i].append(j)   
        seen = set()                          
        def DFS(node):
            if node in seen:            # if we go back to visted node, that means there exist a loop which we can return False
                return False
            if not adjList[node]:       # for the leaf node, if the left node not equals to target, then return False 
                return node == destination
            seen.add(node)              # add the node to the visited part and start the recursion
            for neib in adjList[node]:
                if neib == node or not DFS(neib):
                    return False
            seen.remove(node)           # backtrack part, remove the visited node.
            return True

        return DFS(source)