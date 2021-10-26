class Solution(object):
    def getModifiedArray(self, length, updates):
        """
        :type length: int
        :type updates: List[List[int]]
        :rtype: List[int]
        """
        
        nums = [0]*(length + 1)
        
        for start, end, val in updates:
            nums[start] += val
            nums[end+1] -= val
        
        for i in range(1, len(nums)):
            nums[i] += nums[i-1]
            
        nums.pop()
        return nums


"""
extention for different initilization value
"""
class Solution(object):
    def getModifiedArray(self, arr, updates):
        """
        :type arr: List[int]
        :type updates: List[List[int]]
        :rtype: List[int]
        """

        nums = [0]*(len(arr) + 1)
        
        for start, end, val in updates:
            nums[start] += val
            nums[end+1] -= val
        
        for i in range(1, len(nums)):
            nums[i] += nums[i-1]
            
        nums.pop()
        
        for i in range(len(arr)):
            nums[i] += arr[i]
        
        return nums    
        
class Solution(object):
    def getModifiedArray(self, arr, updates):
        """
        :type arr: List[int]
        :type updates: List[List[int]]
        :rtype: List[int]
        """

        for i in range(len(arr) - 1, 0, -1):
            arr[i] -= arr[i-1]
        
        arr.append(0)
        
        for start, end, val in updates:
            arr[start] += val
            arr[end+1] -= val
        
        for i in range(1, len(arr)):
            arr[i] += arr[i-1]
        
        arr.pop()
        
        return arr