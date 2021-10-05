class Solution:
    def findShortestSubArray(self, nums: List[int]) -> int:
        """
        naive way, two pass
        """
        
        lo = {}
        hi = {}
        degree = 0
        count = {}
        
        for num in nums:
            if num not in count:
                count[num] = 1
            else:
                count[num] += 1
                
        degree = max(count.values())
        
        freq = {}
        result = inf
        
        for i, num in enumerate(nums):
            if count[num] == degree:
                if num not in freq:
                    freq[num] = 1
                else:
                    freq[num] += 1
                if num not in lo:
                    lo[num] = i
                if freq[num] == degree:
                    hi[num] = i
                    result = min(result, hi[num] - lo[num] + 1)
        return result

class Solution:
    def findShortestSubArray(self, nums: List[int]) -> int:
        """
        two pass improved
        """
        lo, hi, count = {}, {}, {}
        
        for i, num in enumerate(nums):
            count[num] = count.get(num, 0) + 1
            if num not in lo:
                lo[num] = i
            hi[num] = i
                
        degree = max(count.values())
        result = inf
        
        for num in count:
            if count[num] == degree:
                result = min(result, hi[num] - lo[num] + 1)
        
        return result

class Solution:
    def findShortestSubArray(self, nums: List[int]) -> int:
        """
        better two pass
        """
        
        ind = collections.defaultdict(list)
        
        degree = 0
        result = inf
        
        for i, num in enumerate(nums):
            ind[num].append(i)
        
        for num in ind:
            degree = max(degree, len(ind[num]))
            
        for _, ls in ind.items():
            if len(ls) == degree:
                result = min(result, ls[-1] - ls[0] + 1)
        
        return result

               
        
class Solution:
    def findShortestSubArray(self, nums: List[int]) -> int:
        """
        one pass
        """
        
        lo, count = {}, {}
        result = 0
        degree = 0
        for i, num in enumerate(nums):
            count[num] = count.get(num, 0) + 1
            lo.setdefault(num, i)
            if count[num] > degree:
                result = i - lo[num] + 1
                degree = count[num]
            elif count[num] == degree:
                result = min(result, i - lo[num] + 1)
        return result
            
