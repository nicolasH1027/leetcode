class Solution:
    def atMostNGivenDigitSet(self, digits: List[str], n: int) -> int:
        
        s = str(n)
        ans, s_len, d = 0, len(s), len(digits)
        
        
        """
        for number that has less digits than n
        """
        
        for i in range(1, s_len):
            ans += d**i
            
            
        """
        for number that has the same number of digits
        """
        for i in range(s_len):
            
            prefix = 0
            
            for c in digits:
                
                # 5xxx, [1,2,3]
                if c < s[i]:
                    ans += d**(s_len - i - 1)

                # """
                # 5xxx, [5,2,3]
                # """
                elif c == s[i]:
                    
                    prefix = 1
                    
                    break
            
            if not prefix:
                return ans

        
        # "The n itself"
        
        return ans + 1