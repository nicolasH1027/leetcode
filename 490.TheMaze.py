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
    

class Solution:
    def hasPath(self, maze: List[List[int]], start: List[int], destination: List[int]) -> bool:
        
        queue = collections.deque()
        queue.append(start)
        m, n, seen = len(maze), len(maze[0]), set(start)
        
        while queue:
            
            i, j = queue.popleft()
            
            if i == destination[0] and j == destination[1]:
                return True
            
            for dx, dy in [[0,1], [1,0], [0,-1], [-1,0]]:
                
                row, col = i + dx, j + dy
                
                while 0 <= row < m and 0 <= col < n and not maze[row][col]:
                    
                    row, col = row + dx, col + dy
                row -= dx
                col -= dy
                
                if (row, col) in seen: continue
                seen.add((row, col))
                queue.append([row, col])
        
        return False
                    