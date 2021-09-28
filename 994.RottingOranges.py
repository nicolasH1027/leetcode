class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        
        queue = collections.deque()
        count = 0
        m = len(grid)
        n = len(grid[0])
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 2:
                    queue.append((i, j))
                if grid[i][j] == 1:
                    count += 1
        result = 0
        seen = set()
        while queue:
            for _ in range(len(queue)):
                row, col = queue.popleft()
                for i, j in [(1,0),(-1,0),(0,1),(0,-1)]:
                    if 0<=row+i<m and 0<=col+j<n and (row+i, col+j) not in seen and grid[row+i][col+j] == 1:
                        seen.add((row+i, col+j))
                        queue.append((row+i, col+j))
                        count -= 1
            result += 1
        
        return max(0, result - 1)  if count == 0 else -1