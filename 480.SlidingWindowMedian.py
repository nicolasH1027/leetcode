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


# class Solution:
#     def medianSlidingWindow(self, nums: List[int], k: int) -> List[float]:
#         "Two Heap"





