class Solution:
    def findLeastNumOfUniqueInts(self, arr: List[int], k: int) -> int:
        
        freq, n = collections.Counter(arr), len(arr)

        ans, cnt = len(freq), collections.Counter(freq.values())
        
        for i in range(1, n + 1):
            
            if k >= i*cnt[i]:
                k -= i*cnt[i]
                ans -= cnt[i]
            else:
                return ans - k // i
            
        return ans