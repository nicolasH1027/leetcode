class Solution:
    def hasPath(self, maze: List[List[int]], start: List[int], destination: List[int]) -> bool:
                
        m, n, seen = len(maze), len(maze[0]), set(start)
        
        direction = [[0,1], [1,0], [0,-1], [-1,0]]

        def dfs(coor):
            
            if coor == destination:
                return True

            for dx, dy in direction:
                i, j = coor
                while 0 <= i + dx < m and 0 <= j + dy < n and not maze[i+dx][j+dy]:   
                    i += dx
                    j += dy
                    
                if (i, j) in seen: continue
                
                seen.add((i, j))
                if dfs([i, j]):
                    return True
                
            return False
        
        return dfs(start)