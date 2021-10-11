class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        
        """
        O(N) time complexity,  O(K) K the max_len space
        """
        
        max_len = 0
        dul = set()
        lpt = 0

        for i in range(len(s)):

            if s[i] not in dul:
                dul.add(s[i])
            else:
                max_len = max(max_len, len(dul))
                for j in range(lpt, i):
                    dul.remove(s[j])
                    lpt += 1
                    if s[j] == s[i]:
                        break
                dul.add(s[i])

        return max(max_len, len(dul))               


class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        
        """
        O(N) time complexity,  O(m) m unique
        """
        
        seen = {}
        ans = 0
        lo = 0

        for hi in range(len(s)):
            
            if s[hi] not in seen:
                ans = max(ans, hi - lo + 1)
            else:
                if seen[s[hi]] < lo:
                    ans = max(ans, hi - lo + 1)
                else:
                    lo = seen[s[hi]] + 1
                
            seen[s[hi]] = hi
            
        return ans