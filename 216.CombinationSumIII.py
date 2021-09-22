class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        "Backtrack"
        result = []
        def backtrack(target, track, k, start):
            
            if target == 0 and k == 0:   # termination condition
                result.append(track[:])
                return
            if target < 0 or k < 0:      # termination condition
                return
            
            for next_val in range(start, 10):           # here, the start is used to make sure that each number can only occur once in each position. 
                track.append(next_val)
                backtrack(target - next_val, track,k - 1, next_val + 1)
                track.pop()
        
        backtrack(n, [], k, 1)
        return result