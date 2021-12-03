from typing import Tuple


class Solution:
    def shortestPathAllKeys(self, grid: List[str]) -> int:
        
        if not grid or not grid[0]: return -1
        
        m, n, all_key, key = len(grid), len(grid[0]), [0]*6, (0,)*6
        
        queue = collections.deque()
        
        for i in range(m):
            for j in range(n):
                if grid[i][j] == '@':
                    queue.append((i, j, tuple(key)))
                elif grid[i][j].islower():
                    all_key[ord(grid[i][j]) - ord('a')] = 1
        
        all_key = tuple(all_key)
        seen = set()
        depth = 0
        
        while queue:
            
            k = len(queue)
            
            for _ in range(k):
            
                i, j, key = queue.popleft()
                
                if key == all_key: return depth
                
                if (i, j, key) in seen: continue
                
                seen.add((i, j, key))
                
                for idx, jdy in [(-1, 0), (1, 0), (0, 1), (0, -1)]:
                    nx, ny, nkey = i + idx, j + jdy, list(key)
                    
                    if nx < 0 or nx >= m or ny < 0 or ny >= n or grid[nx][ny] == '#': continue

                    if grid[nx][ny].isupper() and not nkey[ord(grid[nx][ny]) - ord('A')]: continue
                    
                    if grid[nx][ny].islower(): nkey[ord(grid[nx][ny]) - ord('a')] = 1
                    
                    if (nx, ny, tuple(nkey)) in seen: continue
                    
                    queue.append((nx, ny, tuple(nkey)))

            depth +=1
        
        return -1
        
    