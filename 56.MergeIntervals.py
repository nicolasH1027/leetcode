class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        
        intervals.sort(key = lambda x: x[0])
        
        result = []
        
        for item in intervals:
            
            if not result or result[-1][1] < item[0]:
                result.append(item)
                
            else:
                result[-1][1] = max(result[-1][1], item[1])
        return result    
        
    
    
    