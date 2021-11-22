class Solution:

    def __init__(self, n: int, blacklist: List[int]):
        
        self.dic = {}
        
        self.bound = n - len(blacklist)
        
        pivot = n - 1
        
        for val in blacklist:
            self.dic[val] = -1
        
        for val in blacklist:
            if val < self.bound:
                while pivot in self.dic:
                    pivot -= 1
                self.dic[val] = pivot
                pivot -= 1
                

    def pick(self) -> int:
        
        ind = random.randint(0, self.bound - 1)
        
        if ind in self.dic:
            return self.dic[ind]
        else:
            return ind
        


# Your Solution object will be instantiated and called as such:
# obj = Solution(n, blacklist)
# param_1 = obj.pick()