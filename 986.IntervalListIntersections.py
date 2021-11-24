class Solution:
    def intervalIntersection(self, firstList: List[List[int]], secondList: List[List[int]]) -> List[List[int]]:
        
        ans = []
        
        i = j = 0
        n1, n2 = len(firstList), len(secondList)
        
        while i < n1 and j < n2:
            
            if firstList[i][1] < secondList[j][0]:
                i += 1
                continue
            
            if firstList[i][0] > secondList[j][1]:
                j += 1
                continue
            
            if secondList[j][0] <= firstList[i][1] <= secondList[j][1]:
                
                ans.append([max(firstList[i][0],
                               secondList[j][0]), firstList[i][1]])
                i += 1
                continue
            
            if firstList[i][0] <= secondList[j][1] <= firstList[i][1]:
                
                ans.append([max(firstList[i][0],
                               secondList[j][0]), secondList[j][1]])
                
                j += 1
                continue
            
        return ans
    


class Solution:
    def intervalIntersection(self, firstList: List[List[int]], secondList: List[List[int]]) -> List[List[int]]:
        
        ans = []
        
        i = j = 0
        n1, n2 = len(firstList), len(secondList)
        
        while i < n1 and j < n2:
            
            lo, hi = max(firstList[i][0], secondList[j][0]), min(firstList[i][1], secondList[j][1])
            
            if lo <= hi:
                ans.append([lo, hi])
                
            if firstList[i][1] < secondList[j][1]:
                i += 1
            else:
                j += 1
        
        return ans