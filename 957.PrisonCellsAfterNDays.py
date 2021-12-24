class Solution:
    def prisonAfterNDays(self, cells: List[int], n: int) -> List[int]:
        
        def move(cell):
            return [int(i>0 and i<7 and cell[i-1] == cell[i+1]) for i in range(8)]
        
        state = {}
        
        while n:
            
            cells = tuple(cells)
            
            if cells in state:
                n %= state[cells] - n
            
            state[cells] = n
            
            if n > 0:
                n -= 1
                cells = move(cells)
            
        return cells