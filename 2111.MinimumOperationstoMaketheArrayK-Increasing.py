class Solution:
    def kIncreasing(self, arr: List[int], k: int) -> int:
        
        """
        k*(n/k*log(n/k)) = n*log(n/k)
        """
        
        ans, pt, n = 0, 0, len(arr)
        
        for i in range(k):
            
            sub_len, sub_arr = 0, []
            
            pt = i
            
            while pt < n:
                
                sub_len += 1
                """
                和300题不同的是，这里得用right， 因为每次得把element
                加入到sub_arr的右侧，而300题则是左侧
                """
                pos = bisect.bisect_right(sub_arr, arr[pt])
                
                if pos == len(sub_arr):
                    sub_arr.append(arr[pt])
                else:
                    sub_arr[pos] = arr[pt]
                
                pt += k    
            
            ans += sub_len - len(sub_arr)

        return ans