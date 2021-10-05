class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        """
        O(N) time,  O(N) space
        """
        count = {}
        for num in nums:
            count[num] = count.get(num, 0) + 1
        
        majority = 0
        degree = 0
        
        for num in count:
            if count[num]  > degree:
                degree = count[num]
                majority = num
            
        return majority
    

class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        """
        Boyer-Moore Voting Algorithm
        Because the number of majority element will exceeds n // 2
        """
        
        result = None
        count = 0
        
        for num in nums:
            if count == 0:
                result = num
                
            count += 1 if num == result else - 1
        
        return result 
        