# quick sort 
# without randomization

def quicksort(data, p, r):
    if p < r:
        q = partition(data, p, r)
        quicksort(data, p, q - 1)
        quicksort(data, q + 1, r)

def partition(data, p, r):
    x = data[r]
    i = p - 1
    for j in range(p, r):
        if data[j] <= x:
            i = i + 1
            data[i], data[j] = data[j], data[i]
    data[i+1], data[r] = data[r], data[i+1]
    return i+1    

# quick sort 
# with randomization

import random
from typing import Collection

def quicksort(data, p, r):
    "O(nlog(n)), inplace"
    if p < r:
        q = partition(data, p, r)
        quicksort(data, p, q - 1)
        quicksort(data, q + 1, r)

def partition(data, p, r):
    randIND = random.randint(p, r) 
    data[r], data[randIND] = data[randIND], data[r]
    x = data[r]
    i = p - 1
    for j in range(p, r):
        if data[j] <= x:
            i = i + 1
            data[i], data[j] = data[j], data[i]
    
    data[i+1], data[r] = data[r], data[i+1]
    return i+1  

# merge and sort 

class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        "O(nlog(n))"
        if len(nums) == 1:
            return nums
        
        pivot =  len(nums) // 2
        
        leftpart = self.sortArray(nums[0:pivot])
        rightpart = self.sortArray(nums[pivot:])
        
        return self.merge(leftpart, rightpart)
    
    def merge(self, left, right):
        
        res = []
        lpt = 0
        rpt = 0
        
        m = len(left)
        n = len(right)
        
        while lpt < m and rpt < n:
            if left[lpt] < right[rpt]:
                res.append(left[lpt])
                lpt += 1
            else:
                res.append(right[rpt])
                rpt += 1
        res.extend(left[lpt:])
        res.extend(right[rpt:])
        
        return res
        
        
# bubble sort 

class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        "O(n^2)"
        for i in range(len(nums)-1, 0, -1):
            for j in range(i):
                if nums[j] > nums[j + 1]:
                    nums[j], nums[j+1] = nums[j+1], nums[j]

        return nums
    
    
# heap sort 

class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        "O(nlog(n))"
        heapq.heapify(nums)
        
        result = []
        
        for _ in range(len(nums)):
            result.append(heapq.heappop(nums))
            
        return result
    
# insertion sort

class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        "O(n^2)"
        result = []
        for item in nums:
            bisect.insort_left(result, item)
        
        return result
    
    
# counting sort
# the array is required to be array of inter and we knoe the maximum value

def countsort(nums):
    "O(3*N)only works for positive number, not stable"
    MAX = max(nums)
    MIN = min(nums) 
    count = [0]*(MAX - MIN + 1)
    for item in nums:
        count[item - MIN] += 1
    ind = 0
    for i in range(len(count)):
        while count[i] > 0:
            nums[ind] = i + MIN
            ind += 1
            count[i] -= 1
    return nums

def countsort(nums):
    "O(N), works for negative number, stable"
    MAX = max(nums)
    MIN = min(nums)
    count = [0]*(MAX - MIN + 1)
    
    for item in nums:
        count[item - MIN] += 1

    for i in range(1, len(count)):
        count[i] = count[i] + count[i-1]

    tmp = [0]*len(nums)
    
    for i in range(len(nums) - 1, -1, -1):
        pos = nums[i] - MIN
        sumCount = count[pos]
        
        tmp[sumCount - 1] = nums[i]
        count[pos] -= 1
    return tmp