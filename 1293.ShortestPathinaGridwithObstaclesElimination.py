class Solution:
    def shortestPath(self, grid: List[List[int]], k: int) -> int:
        
        m, n = len(grid), len(grid[0])
        
        if k >= m + n - 2:
            return m + n - 2
        
        queue = collections.deque()
        queue.append((0, 0, k))
        depth = 0
        seen = set((0, 0, k))
        
        while queue:
            
            l = len(queue)
            
            for _ in range(l):
                
                i, j, life = queue.popleft()
                
                if i == m - 1 and j == n - 1:
                    return depth

                for idx, jdy in [(-1, 0), (1, 0), (0, 1), (0, -1)]:
                    nx, ny = i + idx, j + jdy
                    
                    if nx < 0 or nx >= m or ny < 0 or ny >= n: continue
                    
                    newlife = life - grid[nx][ny]
                    
                    if newlife >= 0 and (nx, ny, newlife) not in seen:
                        queue.append((nx, ny, newlife))
                        seen.add((nx, ny, newlife))
            
            depth += 1
            
        return -1