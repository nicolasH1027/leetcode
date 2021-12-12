from binary_search import bisect_left


class Solution:
    def medianSlidingWindow(self, nums: List[int], k: int) -> List[float]:
        "Insertion Sort"
        import bisect
        windows = nums[0:k]
        windows.sort()
        result = []
        for i in range(k, len(nums)):           
            result.append((windows[k//2] + windows[(k - 1)//2]) / 2)
            bisect.insort_left(windows, nums[i])
            ind = bisect.bisect_left(windows, nums[i - k])
            windows.pop(ind)
        result.append((windows[k//2] + windows[(k - 1)//2]) / 2)  # to add the last window median
        return result



class Solution:
    def medianSlidingWindow(self, nums: List[int], k: int) -> List[float]:
        "Two Heap"
        
        lo, hi, mediean = [], [], []
        
        dic = collections.defaultdict(int)
        
        for i in range(k):
            heapq.heappush(lo, -nums[i])
            
        for i in range(k//2):
            heapq.heappush(hi, -heapq.heappop(lo))
        
        mediean.append(-lo[0] if k % 2 else (hi[0] - lo[0])/2)
            
        for i in range(k, len(nums)):
            
            heapq.heappush(lo, -heapq.heappushpop(hi, nums[i]))
            out_num = nums[i - k]
            dic[out_num] += 1
            if out_num > -lo[0]:
                heapq.heappush(hi, -heapq.heappop(lo))
            
            while lo and dic[-lo[0]]:
                dic[-lo[0]] -= 1
                heapq.heappop(lo)
            
            while hi and dic[hi[0]]:
                dic[hi[0]] -= 1
                heapq.heappop(hi)
            
            mediean.append(-lo[0] if k % 2 else (hi[0] - lo[0])/2)
        
        return mediean


