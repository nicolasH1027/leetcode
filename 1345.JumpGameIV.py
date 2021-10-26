class Solution(object):
    def minJumps(self, arr):
        """
        :type arr: List[int]
        :rtype: int
        """
        
        n = len(arr)
        
        if n <= 1:
            return 0
        
        graph = collections.defaultdict(list)
        
        for i, val in enumerate(arr):            
            graph[val].append(i)
        
        queue = collections.deque()
        queue.append(0)
        seen = set()
        seen.add(0)
        step = 0
        
        while queue:

            for _ in range(len(queue)):
          
                node = queue.popleft()
                if node == n - 1:
                    return step

                for child in graph[arr[node]]:
                    if child not in seen:
                        queue.append(child)
                        seen.add(child)

                graph[arr[node]].clear()

                for child in [node-1, node+1]:
                    if 0 <= child < n and child not in seen:
                        queue.append(child)
                        seen.add(child)
            step += 1
            
        return -1
    
# =====================================================================

class Solution(object):
    def minJumps(self, arr):
        """
        :type arr: List[int]
        :rtype: int
        """
        
        n = len(arr)
        
        if n <= 1:
            return 0
        
        graph = collections.defaultdict(list)
        
        for i, val in enumerate(arr):            
            graph[val].append(i)
        
        front = set([0])
        end = set([n-1])
        seen = set([0,n-1])
        step = 0
        
        while front:
            
            if len(end) < len(front):
                end, front = front, end
            
            nex = set()

            for node in front:
                
                for child in graph[arr[node]]:
                    if child in end:
                        return step + 1
                    if child not in seen:
                        nex.add(child)
                        seen.add(child)

                graph[arr[node]].clear()
            
                for child in [node-1, node+1]:
                    if child in end:
                        return step + 1
                    if 0<= child < n and child not in seen:
                        nex.add(child)
                        seen.add(child)

            front = nex
            step += 1
            
        return -1
        