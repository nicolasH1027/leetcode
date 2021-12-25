class Solution:
    def numDistinctIslands(self, grid: List[List[int]]) -> int:
        
        m, n, seen = len(grid), len(grid[0]), set()
        direction = {'r':(1, 0), 'd':(0, -1), 'l':(-1, 0), 'u':(0, 1)}
        
        
        def dfs(coor):
            
            seen.add(coor)
            path = ['#']
            
            i, j = coor
            
            for key, d in direction.items():
                dx, dy = d
                if 0 <= i + dx < m and 0 <= j + dy < n and (i+dx, j+dy) not in seen and grid[i+dx][j+dy]:
                    path.append(key)
                    path.extend(dfs(((i+dx, j+dy))))
            path.append('*')
            return path
        
        ans, land = set(), []
        
        for i in range(m):
            for j in range(n):
                if grid[i][j]:
                    land.append((i, j))
                    
        for cor in land:
            
            if cor in seen: continue
            path = dfs(cor)
            ans.add(''.join(path))
            
        return len(ans)