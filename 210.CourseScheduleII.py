class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        """
        Topological sorting, O(E + V)
        """
        indegree = collections.defaultdict(set)
        outdegree = collections.defaultdict(set)
        
        for child, parent in prerequisites:
            indegree[child].add(parent)
            outdegree[parent].add(child)
            
        queue = collections.deque()
        
        for i in range(numCourses):
            if i not in indegree:
                queue.append(i)
                
        result = []
        while queue:
            cur = queue.leftpop()
            result.append(cur)
            for tar in outdegree[cur]:
                indegree[tar].remove(cur)
                if len(indegree[tar]) == 0:
                    queue.append(tar)
            del outdegree[cur]
        return result if len(result) == numCourses else []
    
class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        """
        DFS, O(E + V)
        """
        # use DFS to parse the course structure
        self.graph = collections.defaultdict(list) # a graph for all courses
        self.res = [] # start from empty
        for pair in prerequisites:
            self.graph[pair[0]].append(pair[1]) 
        self.visited = [0 for x in range(numCourses)] # DAG detection 
        for x in range(numCourses):
            if not self.DFS(x):
                return []
             # continue to search the whole graph
        return self.res
    
    def DFS(self, node):
        if self.visited[node] == -1: # cycle detected
            return False
        if self.visited[node] == 1:
            return True # has been finished, and been added to self.res
        self.visited[node] = -1 # mark as visited
        for x in self.graph[node]:
            if not self.DFS(x):
                return False
        self.visited[node] = 1 # mark as finished
        self.res.append(node) # add to solution as the course depenedent on previous ones
        return True