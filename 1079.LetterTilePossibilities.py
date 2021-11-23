class Solution:
    def numTilePossibilities(self, tiles: str) -> int:
        
        cnt = [0]*26
        
        for c in tiles:
            cnt[ord(c) - ord('A')] += 1
            
        def backtrack(arr):
            ans = 0
            for i in range(len(arr)):
                if arr[i] == 0: continue
                arr[i] -= 1
                ans += 1
                ans += backtrack(arr)
                arr[i] += 1
            return ans

        return backtrack(cnt)
        

