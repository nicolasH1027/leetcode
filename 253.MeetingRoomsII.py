class Solution(object):
    def minMeetingRooms(self, intervals):
        """
        :type intervals: List[List[int]]
        :rtype: int
        """
        
        """
        非常直觉的想法，生活中怎么安排？
        假设第一组人开会，很自然开一间新会议室。
        第二组来了，假如第一组没走，则需新开一间，如果走了
        则使用原来那间（在这题中，我们只关心多少间会议室，而不是哪一间）。
        一次类推，第三组来了，如果前面两组有结束的，那么不需要新开，否则新开一间。
        
        所以，每一次有新的团队要开会，只需要比较所有正在开会的团队的结束时间的最小值，
        就可以确定是否需要新开一间会议室。
        自然而然联想到需要使用 ‘优先队列’ 存储最小的结束时间。，
        
        O(nlogn) time complexity, O(n) space complexity
        """
        
        if not intervals:
            return 0
        
        intervals.sort(key = lambda x: x[0])
        
        heap = []
        heapq.heappush(heap, intervals[0][1])
        
        for i in range(1, len(intervals)):
            
            if intervals[i][0] >= heap[0]:
                heapq.heappop(heap)
            
            heapq.heappush(heap, intervals[i][1])
        
        return len(heap)
    
"""
TWO pointer if we dont want to use priority queue
"""

class Solution(object):
    def minMeetingRooms(self, intervals):
        """
        :type intervals: List[List[int]]
        :rtype: int
        """
        
        if not intervals:
            return 0
        
        start = [x[0] for x in sorted(intervals, key=lambda x: x[0])]  # nlogn
        end = [x[1] for x in sorted(intervals, key=lambda x: x[1])]
        
        cnt = 0
        res = 0
        i, j = 0, 0
        
        while i < len(start):
            
            if start[i] < end[j]:
                i += 1
                cnt += 1
                res = max(res, cnt)
            else:
                j += 1
                cnt -= 1
            
        return res 
            
            