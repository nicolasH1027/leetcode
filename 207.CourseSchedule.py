class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        """
        O(E + v)
        """
        ourdegree = collections.defaultdict(list)
        indegree = {}
        
        for src, tar in prerequisites:
            ourdegree[src].append(tar)
            indegree[tar] = indegree.get(tar, 0) + 1
        
        queue = collections.deque()
        for i in range(numCourses):
            if i not in indegree:
                queue.append(i)
        study = 0
        while queue:
            for _ in range(len(queue)):
                cur = queue.popleft()
                study += 1
                for course in ourdegree[cur]:
                    if course in indegree:  
                        indegree[course] -= 1
                        if indegree[course] == 0:
                            queue.append(course)
        return study == numCourses
        