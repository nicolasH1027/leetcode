"""
扫描线技巧可以用于解决如下若干问题

1854. Maximum Population Year;  Easy
(Lintcode) 391 · Number of Airplanes in the Sky;    Medium
56. Merge Intervals;    Medium
252. Meeting Rooms;     Easy
253. Meeting Rooms II;     Medium
1094. Car Pooling;      Medium
1109. Corporate Flight Bookings：   Medium
370. Range Addition；   Medium
1589. Maximum Sum Obtained of Any Permutation；    Medium
1229. Meeting Scheduler；   Medium
759. Employee Free Time;    Hard
218	The Skyline Problem;    Hard
391	Perfect Rectangle;  Hard
850	Rectangle Area II;  Hard
1851 Minimum Interval to Include Each Query;    Hard
"""

"""
扫描线算法可以用下面的例子进行解释，假设下面最长且连续的是时间轴

-----------------------------------------------------

-----  ----------              ------ ---------
 -------            --------     ---------

然后，假设上面两段不连续的横线是区间段，扫描线算法就是用一条

竖线沿着时间轴扫过去， 遇到端点就进行操作，加一或者减一或者进行区间合并等
"""


"1854. Maximum Population Year;  Easy"
class Solution:
    def maximumPopulation(self, logs: List[List[int]]) -> int:
        population = [0]*101
        "扫描线扫描， 把端点都映射到时间轴上，活着的加一，死了的减一"
        for birth, death in logs:
            population[birth - 1950] += 1
            population[death - 1950] -= 1
            
        ans, maxpop, cnt = 0, -float('inf'), 0
        "因为已经将时间与人数映射到时间轴上，再扫一遍时间轴，就可以知道最大人口是多少了"
        for i, val in enumerate(population):
            cnt += val
            if cnt > maxpop:
                ans = i + 1950
                maxpop = cnt
        return ans

class Solution:
    def maximumPopulation(self, logs: List[List[int]]) -> int:
        "套模板的解法"
        dates = []
        "扫描一遍数据，开始对应1，结束对应-1"
        for date in logs:
            dates.append((date[0], 1))
            dates.append((date[1], -1))
        "排序"
        dates.sort()
        ans, maxpop, cnt = 0, -float('inf'), 0
        for date, val in dates:
            cnt += val
            if cnt > maxpop:
                ans = date
                maxpop = cnt
        return ans
    
"(Lintcode) 391 · Number of Airplanes in the Sky;    Medium"
class Solution:
    """
    @param airplanes: An interval array
    @return: Count of airplanes are in the sky.
    """
    def countOfAirplanes(self, airplanes):
        
        "这道题目和上题一模一样"
        times = []

        "通过扫描线， 把起飞时间和降落时间分别插入list，起飞时间对应1，降落对应-1"
        for item in airplanes:
            times.append((item.start, 1))
            times.append((item.end, -1))

        "排序， 注意，如果时间相同，降落时间必须排在起飞时间前面，不然会出错"
        times.sort()
        cnt, maxnum = 0, 0
        for _, val in times:
            cnt += val
            if cnt > maxnum:
                maxnum = cnt    
        return maxnum
    
"252. Meeting Rooms;     Easy"
class Solution:
    def canAttendMeetings(self, intervals: List[List[int]]) -> bool:
        """
        一样的扫描线， 因为此题只需要返回 T or F，所以我们不用统计数目.
        所以我们不需要去构建新的list，如上两题。我们直接sort intervals。
        """
        prev = -float('inf')
        for begin, end in sorted(intervals):
            if begin < prev:
                return 
            prev = end
        return True
        
"253. Meeting Rooms II"
class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        """
        和第一题一样， 出生代表开会，死亡代表结束，分别对应1和-1，
        然后排序，然后扫描一遍
        """
        times = []
        for begin, end in intervals:
            times.append(begin, 1)
            times.append(end, -1)     
        times.sort()
        cnt, max_num = 0, -float('inf')
        for _, val in times:
            cnt += val
            if cnt > max_num:
                max_num = cnt
        return max_num
    
"1094. Car Pooling;      Medium"
class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        """
        还是一样的模板，一样的套路, 注意，此题因为知道from和to的时间范围，
        事实上我们可以像题目一一样，通过把weight映射到时间线上，从而把时间复杂度
        降低到O（N）
        """
        nums = []
        for weight, src, tar in trips:
            nums.append((src, weight))
            nums.append((tar, -weight))
        nums.sort()
        cnt = 0
        for _, val in nums:
            cnt += val
            if cnt > capacity:
                return False
        return True
    
"1109. Corporate Flight Bookings：   Medium"
class Solution:
    def corpFlightBookings(self, bookings: List[List[int]], n: int) -> List[int]:
        """
        和之前一样，把人数映射到时间轴上，然后再在结束时间的下一个时间减去。最后
        再通过累积和，就能得到最后的结果
        
        注意这里和list初始化为 n + 1,因为最后的结果有可能越界。
        """
        nums = [0]*(n+1)
        for src, tar, val in bookings:
            nums[src-1] += val
            nums[tar] -= val
        
        for i in range(1, n):
            nums[i] += nums[i-1]
        
        return nums[:-1]
    
"""
这道题其实和 370. Range Addition， 一模一样, 对于这类问题，直接在，
start 出加val， 然后在end + 1处减value
"""
class Solution:
    def getModifiedArray(self, length: int, updates: List[List[int]]) -> List[int]:
        nums = [0]*(length + 1)
        for start, end, val in updates:
            nums[start] += val
            nums[end+1] -= val
        for i in range(1, len(nums)):
            nums[i] += nums[i-1]
        return nums[:-1]
    
"1589. Maximum Sum Obtained of Any Permutation；    Medium"
class Solution:
    def maxSumRangeQuery(self, nums: List[int], requests: List[List[int]]) -> int:
        """
        这题的思路其实很直接，把最大的树放在搜素次数最多的地方就可以了。
        
        那么怎么找到各个位置对应的搜索频率呢？ 不就是前面两道题的思路嘛，
        把上一道的 val 改成1 就可以了。然后再求累积和
        """
        n = len(nums)
        freq = [0]*(n+1)
        for src, end in requests:
            freq[src] += 1
            freq[end+1] -= 1
        
        for i in range(1, n):
            freq[i] += freq[i-1]
        
        "代码基本不用换了"
        nums.sort()
        ans = 0
        for i, val in enumerate(sorted(freq[:-1])):
            ans += nums[i]*val
        return ans % (10**9 + 7)
    
"1229. Meeting Scheduler；   Medium"

class Solution:
    def minAvailableDuration(self, slots1: List[List[int]], slots2: List[List[int]], duration: int) -> List[int]:
        "此题还可以用heap来做，其实performance会好一些，但是time complexity是一样的"
        slots = []
        
        """
        下面这个很熟悉了
        """
        for begin, end in slots1:
            if end - begin < duration:
                continue
            slots.append((begin, 1))
            slots.append((end, -1))
        
        for begin, end in slots2:
            if end - begin < duration:
                continue
            slots.append((begin, 1))
            slots.append((end, -1))
        
        "intersect 用来记录我们遇到几个区间了"
        slots.sort()
        intersect = prev = 0
        for date, status in slots:
            if status == 1:     
                intersect += 1
                prev = date
            if status == -1:
                if intersect == 2 and date - prev >= duration:
                    return [prev, prev + duration]
                intersect -= 1
        return []

class Solution:
    def minAvailableDuration(self, slots1: List[List[int]], slots2: List[List[int]], duration: int) -> List[int]:
        "heap的做法"
        slots = list(filter(lambda x: x[1] - x[0] < duration, slots1 + slots2))
        heapq.heapify(slots)
        while len(heap) > 1:
            _, tail = heapq.heappop(slots)
            if tail >= heap[0][0] + duration:
                return [heap[0][0], heap[0][0] + duration]
        return []
    
    
"759. Employee Free Time;    Hard"
"""
# Definition for an Interval.
class Interval:
    def __init__(self, start: int = None, end: int = None):
        self.start = start
        self.end = end
"""
class Solution:
    def employeeFreeTime(self, schedule: '[[Interval]]') -> '[Interval]':
        """
        其实和上面那题思路是一样的, 这里要注意的是， 当start 和 end 出现tie
        的时候，我们把 start 排在前面。不然的话，我们就需要在for loop里面
        增加一个if， 判断区间是否为0。
        如果需要增加整个时间的开始和结束点， 如 0 到 24，
        可以将 （0， 1) (24, 0)加入list中，然后再排序
        """
        times = []
        for interval in schedule:
            for item in interval:
                times.append((item.start, 0))
                times.append((item.end, 1))
        times.sort()
        ans, intersect, prev = [], 0, None
        for slot, flag in times:
            if not intersect and prev:
                ans.append(Interval(prev, slot))
            if flag:
                intersect -= 1
                prev = slot
            else:
                intersect += 1
        return ans
    
"218. The Skyline Problem；   Hard"

class Solution:
    def getSkyline(self, buildings: List[List[int]]) -> List[List[int]]:
        """
        几个月之前，我觉得这题特别难，但是现在，依旧很难，但是其实，
        通过前面总结的模板，我们还是可以通过套用模板进行突破。
        
        下面是官方题解的描述，我用代码一句一句进行翻译。
        
        观察题目我们可以发现，关键点的横坐标总是落在建筑的左右边缘上。
        这样我们可以只考虑每一座建筑的边缘作为横坐标，这样其对应的纵坐标为「包含该横坐标」的所有建筑的最大高度。
        观察示例一可以发现，当关键点为某建筑的右边缘时，该建筑的高度对关键点的纵坐标是没有贡献的。
        例如图中横坐标为7的关键点，虽然它落在红色建筑的右边缘，但红色建筑对其并纵坐标并没有贡献。
        因此我们给出「包含该横坐标」的定义：建筑的左边缘小于等于该横坐标，右边缘大于该横坐标（也就是我们不考虑建筑的右边缘）。
        即对于包含横坐标 x 的建筑 i，有 x∈[left_i, right_i)。

        特别地，在部分情况下，「包含该横坐标」的建筑并不存在。例如当图中只有一座建筑时，该建筑的左右边缘均对应一个关键点，
        当横坐标为其右边缘时，这唯一的建筑对其纵坐标没有贡献。因此该横坐标对应的纵坐标的大小为 0。
        
        这样我们可以想到一个暴力的算法：O(n)地枚举建筑的每一个边缘作为关键点的横坐标，过程中我们 O(n) 地检查每一座建筑是否「包含该横坐标」，
        找到最大高度，即为该关键点的纵坐标。该算法的时间复杂度是 O(n^2)，我们需要进行优化。
        """
        
        """
        暴力解法从左向右枚举每一个边缘， 这句话代表我们得对数据进行排序，然后根据每个点对应的高度，进行下一步处理
        这样的思路，我们可以用扫描线技巧去处理 nlogn
        """
        
        build = []
        for l, r, h in buildings:
            """
            -h 是因为排序的时候，我们希望越高的建筑越在前面。
            为什么把 r也加进l的tuple中去？
            因为每次遍历的时候，我们需要判断l是不是在范围内？
            即对于包含横坐标 l 的建筑 i，有 x∈[left_i, right_i)。
            所以这里，我们需要把右端点放入list中，以便之后我们把每一个l
            对应的h和r放入优先队列中。
            """
            build.append((l, -h, r))
            build.append((r, 0, 0))
        build.sort()
        "skyline和队列中的初始值是为了方便之后的比较，下文有解释"
        skyline, queue = [(0, 0)], [(0, float('inf'))] 
        for l, h, r in build:
            while l >= queue[0][1]:
                heapq.heappop(queue)
            if h:
                heapq.heappush(queue, (h, r))
            if skyline[-1][1] != -queue[0][0]:
                skyline.append((l, -queue[0][0]))
        return skyline[1:]