class Solution:
    def minimumSemesters(self, n: int, relations: List[List[int]]) -> int:
        """
        O(n + E)
        """
        outdegree = collections.defaultdict(list)
        indegree = collections.defaultdict(dict)
        for src, tar in relations:
            outdegree[src-1].append(tar-1)
            if tar-1 not in indegree:
                indegree[tar - 1] = 1
            else:
                indegree[tar - 1] += 1
            
        queue = collections.deque()
        for i in range(n):
            if i not in indegree:
                queue.append(i)
        count = 0
        study = 0
        while queue:
            count += 1
            study += len(queue)
            for _ in range(len(queue)):
                cur = queue.popleft()
                for node in outdegree[cur]:
                    indegree[node] -= 1
                    if indegree[node] == 0:
                        queue.append(node)
        return count if study == n else -1