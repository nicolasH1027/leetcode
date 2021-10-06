class Solution:
    def maximumUnits(self, boxTypes: List[List[int]], truckSize: int) -> int:
        """
        O(nlogn + truckSize), n = len(boxTypes)
        """
        result = 0
        item = 0
        for num, val in sorted(boxTypes,key = lambda x: x[1] ,reverse = True):
            for i in range(num):
                item += 1
                if item > truckSize:
                    return result
                result += val
        return result
    
class Solution:
    def maximumUnits(self, boxTypes: List[List[int]], truckSize: int) -> int:
        """
        O(nlogn), n = len(boxTypes), O(1) space
        """
        result = 0
        for num, val in sorted(boxTypes,key = lambda x: x[1] ,reverse = True):
            if num == truckSize:
                result += num*val
                return result
            elif num < truckSize:
                result += num*val
            else:
                result += truckSize*val
                return result
            truckSize -= num
        return result
    

class Solution:
    def maximumUnits(self, boxTypes: List[List[int]], truckSize: int) -> int:
        """
        O(n), count sort.       O(n) space
        """
        boxes = [0]*1001
        for item, val in boxTypes:
            boxes[val] += item
        
        pt, result = 1000, 0
        
        while truckSize and pt > 0:
            if boxes[pt] == 0:
                pt -= 1
                continue
            if boxes[pt] <= truckSize:
                result += pt*boxes[pt]
                truckSize -= boxes[pt]
                pt -= 1
            else:
                result += truckSize*pt
                truckSize = 0
        return result
        