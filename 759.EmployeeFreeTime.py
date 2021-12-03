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

        ans = []
        end = interval[0].end
        
        for i in range(1, len(interval)):
            
            if interval[i].start > end:
                tmp = Interval(end, interval[i].start)
                ans.append(tmp)
                end = interval[i].end
            else:
                end = max(end, interval[i].end)
        return ans
            
        
        