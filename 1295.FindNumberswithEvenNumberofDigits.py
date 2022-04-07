class Solution:
    def findNumbers(self, nums: List[int]) -> int:
        
        ans = 0
        
        for num in nums:
            
            if len(str(num)) % 2 == 0:
                ans += 1
        
        return 
    
    
class Solution:
    def findNumbers(self, nums: List[int]) -> int:
        
        ans = 0
        
        for num in nums:
            if (math.floor(math.log10(num)) + 1) % 2 == 0:
                ans += 1
                
        return ans
            
        