class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        n1, n2 = len(nums1), len(nums2)
        if n1 > n2:
            return self.findMedianSortedArrays(nums2, nums1)
        
        k = (n1 + n2 + 1) // 2
        
        l = 0
        r = n1
        
        while l < r:
            m1 = l + (r - l) // 2
            m2 = k - m1
            
            if nums1[m1] < nums2[m2 - 1]:
                l = m1 + 1
            else:
                r = m1
        m1 = l
        m2 = k - m1
        
        if m1 <= 0:
            ans11 = -inf
        else:
            ans11 = nums1[m1 - 1]            
            
        if m2 <= 0:
            ans21 = -inf
        else:
            ans21 = nums2[m2 - 1]            
            
        c1 = max(ans11, ans21)
                
        if (n1 +  n2) % 2 == 1:
            return c1
        else:
            
            if m1 >= n1:
                ans12 = inf
            else:
                ans12 = nums1[m1]
                
            if m2 >= n2:
                ans22 = inf
            else:
                ans22 = nums2[m2]           
            
            return (c1 + min(ans12, ans22)) / 2