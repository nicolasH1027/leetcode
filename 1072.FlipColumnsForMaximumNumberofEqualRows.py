class Solution:
    def maxEqualRowsAfterFlips(self, matrix: List[List[int]]) -> int:
        
        pattern = [tuple(x ^ r[0] for x in r) for r in matrix]
        
        return max(Counter(pattern).values())