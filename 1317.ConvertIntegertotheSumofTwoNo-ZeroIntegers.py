class Solution:
    def getNoZeroIntegers(self, n: int) -> List[int]:
        
        a = 1
        
        while '0' in f'{a}{n-1}':
            
            a += 1
            
        return [a, n-1]