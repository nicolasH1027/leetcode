class RangeFreqQuery:

    def __init__(self, arr: List[int]):
        
        self.dic = collections.defaultdict(list)
        
        for i, val in enumerate(arr):
            self.dic[val].append(i)

    def query(self, left: int, right: int, value: int) -> int:
        
        return bisect.bisect_right(self.dic[value], right) - bisect.bisect_left(self.dic[value], left)


# Your RangeFreqQuery object will be instantiated and called as such:
# obj = RangeFreqQuery(arr)
# param_1 = obj.query(left,right,value)