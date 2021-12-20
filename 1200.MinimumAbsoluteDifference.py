class Solution:
    def minimumAbsDifference(self, arr: List[int]) -> List[List[int]]:
        
        arr.sort()
        
        dif = float('inf')
        ans = []
        
        for i in range(len(arr) - 1):
            tmp = arr[i+1] - arr[i]
            if tmp < dif:
                ans = [[arr[i], arr[i+1]]]
                dif = tmp
                
            elif tmp == dif:
                ans.append([arr[i], arr[i+1]])
                
            else:
                continue
        
        return ans
    

class Solution:
    def minimumAbsDifference(self, arr: List[int]) -> List[List[int]]:
        
        maxEle = max(arr)
        minEle = min(arr)
        
        nums = [0]*(maxEle - minEle + 1)
        
        for val in arr:
            nums[val - minEle] = 1
            
        dif = maxEle - minEle
        ans, prev = [], 0

        for i in range(1,len(nums)):

            if not nums[i]: continue
            
            if i - prev < dif:
                ans = [[prev+minEle, i+minEle]]
                dif = i - prev
            elif i - prev == dif:
                ans.append([prev+minEle, i+minEle])
            prev = i
        return ans