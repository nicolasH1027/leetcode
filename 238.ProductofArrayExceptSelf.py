class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        
        """
        O(3N) time, O(2N) space
        """
        n = len(nums)
        left = [1]*n
        right = [1]*n
        
        for i in range(1, n):
            left[i] = nums[i-1]*left[i-1]
            
        for i in range(n-2, -1, -1):
            right[i] = nums[i+1]*right[i+1]
        res = [0]*n
        for i in range(n):
            res[i] = left[i]*right[i]
            
        return res
    
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        
        """
        O(3N) time, O(1) space
        """
        n = len(nums)
        res = [1]*n
        
        for i in range(1,n):
            res[i] = res[i-1]*nums[i-1]

        R = 1
        for i in range(n-1, -1, -1):
            res[i] = res[i]*R
            R *= nums[i]
        return res