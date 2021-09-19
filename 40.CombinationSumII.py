from _typeshed import StrPath
from typing import Counter


class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        "using index and sorting"
        def backtracking(target, start, ls):         # each depth can be treated as the position
            if target == 0:                          # we allow each position to use the same number only once !!!
                result.append(ls[:])
                return
            if target < 0:
                return 
            for i in range(start, len(candidates)):
                if i > start and candidates[i] == candidates[i-1]:continue
                ls.append(candidates[i])
                backtracking(target - candidates[i], i+1, ls)
                ls.pop()
            
        result = []
        candidates.sort()
        backtracking(target, 0, [])
        return result

class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        "using counter"
        
        def backtracking(target, cur, counter, ls):
            if target == 0:
                result.append(ls[:])
                return
            if target < 0:
                return
            
            for next_cur in range(cur, len(counter)):
                candidate, freq = counter[next_cur]
                
                if freq <= 0:
                    continue
                
                ls.append(candidate)
                counter[next_cur] = (candidate, freq - 1)
                
                backtracking(target - candidate, next_cur, counter, ls)
                ls.pop()
                counter[next_cur] = (candidate, freq )
        
        result = []
        counter = Counter(candidates)
        counter = [(c, counter[c]) for c in counter]
        backtracking(target, 0, counter, [])
        return result