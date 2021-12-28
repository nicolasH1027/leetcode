class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        
        max_area, seen = 0, set()
        m, n = len(grid), len(grid[0])
        
        def dfs(i, j):
            
            cnt = 1
            seen.add((i, j))
            
            for dx, dy in [(-1,0), (1,0), (0,1), (0,-1)]:
                if 0 <= i+dx < m and 0 <= j+dy < n and (i+dx,j+dy) not in seen and grid[i+dx][j+dy]:
                    cnt += dfs(i+dx, j+dy)
            return cnt
                  
        for i in range(m):
            for j in range(n):
                if (i, j) in seen: continue
                if not grid[i][j]:
                    seen.add((i, j))
                else:
                    max_area = max(max_area, dfs(i, j))

        return max_area
                

class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        
        max_area, seen = 0, set()
        m, n = len(grid), len(grid[0])
        
        for i in range(m):
            for j in range(n):
                
                if (i, j) in seen: continue
                if not grid[i][j]:
                    seen.add((i,j))
                else:
                    cnt, stack = 0, [(i, j)]
                    seen.add((i, j))
                    while stack:
                        row, col = stack.pop()
                        cnt += 1
                        
                        for dx, dy in [(-1,0), (1,0), (0,1), (0,-1)]:
                            if 0 <= row + dx < m and 0 <= col + dy < n and (row + dx, col + dy) not in seen and grid[row + dx][col + dy]:
                                stack.append((row + dx, col + dy))
                                seen.add((row + dx, col + dy))
                    max_area = max(max_area, cnt)
        
        return max_area
                        
                    
                    
                
                