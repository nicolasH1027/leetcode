class Solution:
    def kSmallestPairs(self, nums1: List[int], nums2: List[int], k: int) -> List[List[int]]:

        if k > len(nums1) * len(nums2):
            k = len(nums1) * len(nums2)
            
        heap = [[nums1[0] + nums2[0], 0, 0]]
        heapq.heapify(heap)
        ans = []
        
        while heap and len(ans) < k:
            
            _, i, j = heapq.heappop(heap)
            
            ans.append([nums1[i], nums2[j]])
            
            if 0 <= i < len(nums1) and 0 <= j < len(nums2) - 1:
                heapq.heappush(heap, [nums1[i] + nums2[j+1], i, j + 1])
            
            if j == 0:
                if 0 <= i < len(nums1) - 1 and 0 <= j < len(nums2):
                    heapq.heappush(heap, [nums1[i+1] + nums2[0], i+1, 0])

        return ans
        