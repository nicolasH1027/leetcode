"""
# Definition for an Interval.
class Interval:
    def __init__(self, start: int = None, end: int = None):
        self.start = start
        self.end = end
"""

class Solution:
    def employeeFreeTime(self, schedule: '[[Interval]]') -> '[Interval]':
        
        interval = sorted([ j for item in schedule for j in item], key = lambda x: x.start)

        res = []
        merge = []
        
        for item in interval:
            
            if not merge:
                merge.append(item)
            elif merge and merge[-1].end < item.start:
                tmp = Interval(merge[-1].end, item.start)
                res.append(tmp)
                merge.append(item)   
            else:
                merge[-1].end = max(merge[-1].end, item.end)
                
        return res