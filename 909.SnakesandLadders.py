class Solution:
    def snakesAndLadders(self, board: List[List[int]]) -> int:
        queue, n = collections.deque([(1, 0)]), len(board)
        seen = set([1])
        
        while queue:
            cur, step = queue.popleft()
            for i in range(1, 7):
                nxt = cur + i
                r, c = divmod(nxt - 1, n) 
                tar = board[~r][c if r % 2 == 0 else ~c]     
                if tar > 0: nxt = tar    
                if nxt == n*n: return step + 1    
                if nxt in seen: continue 
                queue.append((nxt, step + 1))
                seen.add(nxt)
        return -1