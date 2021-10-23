class Solution(object):
    def getFood(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """
        
        queue = collections.deque()
        
        m = len(grid)
        n = len(grid[0])
        seen = set()
        
        for i in range(m):
            for j in range(n):
                if grid[i][j] == '*':
                    queue.append((i, j, 0))
                    break
        
        while queue:
            
            row, col, level = queue.popleft()
            if (row, col) in seen: continue
            seen.add((row, col))
            for i, j in [(0,1), (0,-1), (1,0), (-1,0)]:
                if (row+i, col+j) in seen: continue
                if 0 <= row+i < m and 0 <= col+j < n:
                    if grid[row+i][col+j] == '#':
                        return level + 1
                    elif grid[row+i][col+j] == 'O':
                        queue.append((row+i, col+j, level + 1))
                    else:
                        seen.add((row+i, col+j))
        
        return -1
            
            
            
[
["O","O","O"],
["O","#","#"],
["O","O","X"],
["O","O","O"],
["#","O","*"]]