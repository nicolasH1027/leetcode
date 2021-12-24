class FirstUnique:

    def __init__(self, nums: List[int]):
        
        self.cnt = collections.Counter(nums)
        self.unique = collections.OrderedDict()
        
        for num in nums:
            if self.cnt[num] == 1:
                self.unique[num] = True
        
    def showFirstUnique(self) -> int:
        
        if self.unique:
            return next(iter(self.unique))
        return -1

    def add(self, value: int) -> None:
        
        self.cnt[value] += 1
        
        if self.cnt[value] == 1:
            self.unique[value] = True
        else:
            if value in self.unique:
                del self.unique[value]


# Your FirstUnique object will be instantiated and called as such:
# obj = FirstUnique(nums)
# param_1 = obj.showFirstUnique()
# obj.add(value)


class FirstUnique:

    def __init__(self, nums: List[int]):
        self.queue = collections.deque()
        self.unique = {}
        
        for num in nums:
            self.add(num)
        
    def showFirstUnique(self) -> int:

        while self.queue and not self.unique[self.queue[0]]:
            self.queue.popleft()
        
        if self.queue:
            return self.queue[0]
        return -1
        
    def add(self, value: int) -> None:
        
        self.queue.append(value)
        if value not in self.unique:
            self.unique[value] = True
        else:
            self.unique[value] = False
        


# Your FirstUnique object will be instantiated and called as such:
# obj = FirstUnique(nums)
# param_1 = obj.showFirstUnique()
# obj.add(value)