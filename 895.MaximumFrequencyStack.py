class FreqStack:

    def __init__(self):
        self.freq = {}
        self.group = collections.defaultdict(list)
        self._maxfreq = 0

    def push(self, val: int) -> None:
        self.freq[val] = self.freq.get(val, 0) + 1
        self.group[self.freq[val]].append(val)
        self._maxfreq = max(self._maxfreq, self.freq[val])

    def pop(self) -> int:
        x = self.group[self._maxfreq].pop()
        self.freq[x] -= 1
        if not self.group[self._maxfreq]:
            del self.group[self._maxfreq]
            self._maxfreq -= 1
        return x
        
        
        
        


# Your FreqStack object will be instantiated and called as such:
# obj = FreqStack()
# obj.push(val)
# param_2 = obj.pop()