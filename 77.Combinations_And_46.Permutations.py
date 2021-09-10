class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        
        self.result = []
        self.comb = []
        
        def backtrack(start , k):
            if len(self.comb) == k:
                self.result.append(self.comb[:])
            
            for i in range(start, n+1):
                self.comb.append(i)
                backtrack(start+1, k)
                self.comb.pop()
        backtrack(1, k)
        return 



class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        self.track = set()
        self.per = []
        self.res = []
        self.backtrack(nums, self.track)
        return self.res
    
    def backtrack(self, nums, track):
        
        if len(track) == len(nums):
            self.res.append(self.per[:])
            return 
    
        for i in range(len(nums)):
            if nums[i] in self.track:
                continue
            track.add(nums[i])
            self.per.append(nums[i])
            self.backtrack(nums, self.track)
            self.per.pop()
            track.remove(nums[i])
            
            
        
        
        
        
        
        
        
        
        

