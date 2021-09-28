class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        """
        Here we need to find shortest path, so we can use BFS
        dfs would be out of memory
        """
        n = len(grid)
        # we first remove special cases 
        if grid[0][0] == 1 or grid[n-1][n-1] == 1:
            return -1
        
        # bfs
        queue = collections.deque()
        queue.append([0, 0, 1])
        seen = set((0,0))
        
        while queue:
            row, col, step = queue.popleft()
            if row == n -1 and col == n -1:
                return step
            for i, j in [(1,0), (-1,0), (0,1), (0,-1), (1,1), (-1,-1), (1,-1), (-1,1)]:
                if 0<= row+i < n and 0<= col+j < n and (row+i, col+j) not in seen and grid[row+i][col+j] == 0:
                    queue.append([row + i, col +j, step + 1])
                    seen.add((row+i, col+j))
        return -1
        