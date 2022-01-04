"""
任务分配问题

此类问题一般要求你对不同的任务进行时间上的划分，同时伴有约束条件，
相同任务之间必须间隔 k 个不同的任务，最后问你需要多少时间来完成。

读完下方讲解，你可以轻松秒杀如下几道题
621. Task Scheduler
1953. Maximum Number of Weeks for Which You Can Work
767. Reorganize String
358. Rearrange String k Distance Apart
"""


"""
假设我们有如下若干的任务，如果让我们安排工作，相邻的两个工作不能相等，请问最多我们能完成多少？
严格数学证明请参考 
https://leetcode-cn.com/problems/maximum-number-of-weeks-for-which-you-can-work/solution/ni-ke-yi-gong-zuo-de-zui-da-zhou-shu-by-rbidw/

aaaaabbcd

我们第一步，就是探讨频率最大的工作数量情况
第一步
如果频率最大的工作其频率大于总数的一半
sum - max < max
首先安排最大的
a ___ a ___ a ___ a ___ a ___
然后只需要把剩下的工作一个个填充到空格上
a b | a b | a c | a d | a

res = sum - max,  (bbcd)
很明显， 我们只能完成  2*rest + 1

如果频率最大的工作其频率不超过总数的一半
如 aaabbcd

a b a b a c d

直觉思考， 如果其它项目加起来比最长的项目长，那么一定能够找出k个项目填充频率最大的项目之间的空隙。 剩下的第二大的，同理也可以插入。
最后我们一定能完成所有任务。

所以总的结果就是  min(2*rest + 1, sum)
严格证明参考上述链接

"""

"1953. Maximum Number of Weeks for Which You Can Work"
class Solution:
    def numberOfWeeks(self, milestones: List[int]) -> int:
        
        total = sum(milestones)
        max_val = max(milestones)
        
        if total - max_val < max_val:
            return 2*(total - max_val) + 1
        else:
            return total
        
"621. Task Scheduler"
"""
这道题有一个不同的地方，那就是可以选择一个空位去代替具体的任务。如果这样的话
那其实只需要参考拥有最大频率的任务就可以了
所以总的结果就是  min((k+1)*(max-1) + cnt, sum)

a b idle | a b c | a b

cnt 指的是拥有与最大频率相同频率的任务的个数
"""
class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        
        freq = [0]*26
        
        for task in tasks:
            freq[ord(task) - ord('A')] += 1
        
        hi = max(freq)
        
        cnt = 0
        
        for item in freq:
            if item == hi:
                cnt += 1
        
        return max(len(tasks), (hi-1)*(n+1) + cnt)
    

"358. Rearrange String k Distance Apart"

"""
这道题其实和前面621 其实已经很像了，不同的是没有一个空格让我们进行插入

但是621的(hi-1)*(n+1) + cnt可以作为一个判断条件， 帮我们实现一定的省略部分的计算。

答案需要我们用到两种数据结构，一个是优先队列， 一个是队列

第一步， 算出每个字符对应的频率

a 3, b 2, c 1

接下来最自然的放置方法就是
a

a b

a b c

a b c a

a b c a b

a b c a b  此时为满足条件的最长字符串了（具体证明看第二题）

如何模拟这个过程呢？ 首先，每一次， 我们都拿出频率最大的那个字符串

有哪个数据结果能够帮我们做这个？ 优先队列（log n）

拿完之后呢？ 我们需要一个容器帮我们存刚用过的那个字符串以及对应的频率，并且
在满足k个间隔之后，再次取出最开始放进去的 字符串以及对应的频率， 什么数据结构
能满足这样的时间顺序结构？ 队列！
"""

class Solution:
    def rearrangeString(self, s: str, k: int) -> str:
        
        heap, cnt = [], collections.Counter(s)
        
        
        # 实际测试后速度更慢，可加可不加， 加了就不需要在最后面再加判断了
        # maxcnt = max(cnt.values())
        # if (maxcnt - 1) * k + list(cnt.values()).count(maxcnt) > len(s):
        #     return ""
        
        "因为python只有最小堆，所以加个符号让它成为最大堆"
        for key, count in cnt.items():
            heapq.heappush(heap, (-count, key))

        ans, queue = [], collections.deque()
        
        while heap:
            
            
            cur, key = heapq.heappop(heap)
            "因为是负的，所以加一，代表用掉了一个"
            cur += 1
            ans.append(key)
            queue.append((cur, key))

            "大于号是为了解决 k = 0 的情况"
            if len(queue) >= k:
                cur, key = queue.popleft()
                if cur:
                    heapq.heappush(heap, (cur, key))

        return ''.join(ans) if len(ans) == len(s) else ''
    
    
"767. Reorganize String"

"""
这题其实我们完全可以用上一题的思路去做， 一模一样，把 k 改成2 就可以了

注意， 因为最多只有26个小写字母，这题的复杂度是 n*log(26), 应该是O(n)
"""
class Solution:
    def reorganizeString(self, s: str) -> str:
        
        heap, cnt = [], collections.Counter(s)
        
        
        # 实际测试后速度更慢，可加可不加， 加了就不需要在最后面再加判断了
        # maxcnt = max(cnt.values())
        # if (maxcnt - 1) * k + list(cnt.values()).count(maxcnt) > len(s):
        #     return ""
        
        "因为python只有最小堆，所以加个符号让它成为最大堆"
        for key, count in cnt.items():
            heapq.heappush(heap, (-count, key))

        ans, queue = [], collections.deque()
        
        while heap:
            
            
            cur, key = heapq.heappop(heap)
            "因为是负的，所以加一，代表用掉了一个"
            cur += 1
            ans.append(key)
            queue.append((cur, key))

            "大于号是为了解决 k = 0 的情况"
            if len(queue) >= 2:
                cur, key = queue.popleft()
                if cur:
                    heapq.heappush(heap, (cur, key))

        return ''.join(ans) if len(ans) == len(s) else ''

"""
换一种写法
"""
class Solution:
    def reorganizeString(self, s: str) -> str:
        
        "先填充偶数位的，填满了就填奇数位的"
        
        freq, n = collections.Counter(s), len(s)
        for val in freq.values():
            if val > (n + 1) // 2:
                return ''
        
        odd, even, half = 1, 0, n // 2
        
        ans = [0]*n
        
        for key, count in freq.items():
            
            while count and count <= half and odd < n:
                ans[odd] = key
                count -= 1
                odd += 2
                
            while count:
                ans[even] = key
                count -= 1
                even += 2
        
        return ''.join(ans)
                
            
        
        