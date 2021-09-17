class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        
        def backtracking(target, start, ls):
            if target == 0:
                result.append(ls[:])
                return
            if target < 0:
                return 
            for i in range(start, len(candidates)):            # for the constraint part, check problem 77. combinations, in that problem, to remove dulplicate, we iterate from 
                ls.append(candidates[i])                       # start + 1, however, in this problem, dulplicates are allowed, so we start from start
                backtracking(target - candidates[i], i, ls)
                ls.pop()
            return
        result = []
        backtracking(target, 0, [])
        return result
            