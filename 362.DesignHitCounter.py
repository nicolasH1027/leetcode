class HitCounter:

    def __init__(self):
        self.cnt = 0
        self.queue = collections.deque()

    def hit(self, timestamp: int) -> None:
        self.queue.append(timestamp)

    def getHits(self, timestamp: int) -> int:
        

        while self.queue and timestamp - self.queue[0] >= 300:
            self.queue.popleft()

        return len(self.queue)
        


# Your HitCounter object will be instantiated and called as such:
# obj = HitCounter()
# obj.hit(timestamp)
# param_2 = obj.getHits(timestamp)

class HitCounter:

    def __init__(self):
        self.cnt = [(0, 0)] * 300

    def hit(self, timestamp: int) -> None:
        
        ind = timestamp % 300
        time, ct = self.cnt[ind]
        if time != timestamp:
            self.cnt[ind] = timestamp, 1
        else:
            self.cnt[ind] = time, ct+1
        

    def getHits(self, timestamp: int) -> int:
        
        res = 0
        
        for time, ct in self.cnt:
            if timestamp - time < 300:
                res += ct
        
        return res
        


# Your HitCounter object will be instantiated and called as such:
# obj = HitCounter()
# obj.hit(timestamp)
# param_2 = obj.getHits(timestamp)