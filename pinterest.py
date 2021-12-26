"""
Generally, for BFS, we should mark a node when it is enqueued, not when we visit it.
"""


# 1. 給定一堆blacklist字串List<String>
# 舉例
# [ "machine guns", "terrorist activity", "muder"]

# 2. 一個input sentence
# Ex1.
# "I bought a couple of machine guns yesterday."  return true
# E‍‌‍‍‌‍‌‍‍‌‌‍‌‌‍‍‍‌‌‌x2.
# "I suspect that man is a murderer." return false 必須是一個完整的字匹配，也就是匹配後面必定是空白

# 1. 如果blacklist phrases特别多，一个server放不下怎么办
# 2‍‌‍‍‌‍‌‍‍‌‌‍‌‌‍‍‍‌‌‌. 比较online和offline processing pros and cons
# 3. 有什么string algorithm可以detect？这题我不懂，面试官说没关系，这个非常specific


blacklist = [ "machine guns", "terrorist activity", "murder"]
sentence = "I bought a couple of machine guns yesterday."

trie = {}
END = 'end'

for word in blacklist:
    node = trie
    for letter in word:
        node = node.setdefault(letter, {})
    node[END] = END
    

node = trie
for ind in range(len(sentence)):
    if sentence[ind] not in node:
        node = trie
    else:
        node = node[sentence[ind]]
        if END in node:
            print(node)
            if ind == len(sentence) - 1 or sentence[ind+1] == ' ' or sentence[ind+1] == '.':
            # if ind == len(sentence) - 1 or not sentence[ind+1].isalpha():
                return True
            elif sentence[ind+1] in node:
              continue
            else:
              node = trie
print(False) 


# function getEndpoint(string): string

# | Pattern                      | Endpoint name            |
# |------------------------------|--------------------------|
# | GET /users                   | get_all_users            |
# | GET /users/<UID>             | get_user                 |
# | GET /users/<UID>/preferences | get_user_preferences     |
# | GET /users/<UID>/<UID>       | get_user_posts_in_thread |
# | GET /thread/<UID>            | get_thread               |
# | GET /thread/<UID>/comments   | get_thread_comments      |
# | GET /thread/<UID>/likes      | get_thread_likes         |
# | POST /thread                 | create_thread            |
# | DELETE /comments/<UID>       | delete_comment           |
# | ...                          | ...                      |


# function getEndpoint(string): string

# | Input: String                                   | Expected output     |
# |-------------------------------------------------|----‍‌‍‍‌‍‌‍‍‌‌‍‌‌‍‍‍‌‌‌------------------|
# | GET /users                                      | get_all_users        |
# | GET /users/abc123                               | get_user             |
# | GET /users/def456                               | get_user             |
# | GET /users/thisuseridlookslikewords/preferences | get_user_preferences |
# | GET /thread/thisthreadidlookslikewords/comments | get_thread_comments  |
# | ...                                             | ...                  |

blacklist = [ "GET /users", "GET /users/<UID>", "GET /users/<UID>/preferences", "GET /users/<UID>/<UID>"]
endpoint = ['get_all_users', 'get_user', 'get_user_preferences', 'get_user_posts_in_thread']

Trie = {}
END = 'END'

for pattern, endname in zip(blacklist, endpoint):
    tmp = pattern.split('/')
    node = Trie
    for word in tmp:
        node = node.setdefault(word, {})
    node['Endpoint'] = endname
    

string = 'GET /users/abc123/abc123'
tmp = string.split('/')

node = Trie
for word in tmp:
    if word in node:
        node = node[word]
    else:
        node = node['<UID>']
print(node['Endpoint'])

#------------------------------------------------------------------------------------------------------ split 

import datetime

l1 = ["2021-11-15","2021-11-13","2021-11-10","2021-05-28","2021-06-02","2021-06-02","2021-11-02"]
l2 = ["2021-11-11","2021-03-02","2021-11-05","2021-05-20","2021-05-01","2021-06-01","2021-04-08"]

dt = "2021-11-15"
dt = datetime.strptime(dt, '%Y-%m-%d')
cnt1, cnt2 = 0, 0

for i, j in zip(l1, l2):
  if 0 <= dt - datetime.strptime(i, '%Y-%m-%d') < 7:
    cnt1 += 1
  if 0 <= dt - datetime.strptime(j, '%Y-%m-%d') < 7:
    cnt2 += 1



# # if  user visited Pinterest webpage,
# # possible actions are like the following
# """
# |---register_button (10)  # it means 10 users clicked register_button
# |    |---register_email (5)
# |    |    |---email_already_exists (2)
# |    |    |---register_success (3)
# |    |---register_facebook (4)
# |    |    |---register_success (3)
# |    |---dropoff (2)  # dropoff means that the user clicked the register button but then dorpped off after
# |---login_button (10)
# |    |---login_email (4)
# |    |    |---login_success (4)
# |    |---login_facebook (4)
# |    |    |---login_success (3)
# |    |    |---login_failure (1)
# |    |---dropoff (2)
# """
# # given a string ,build a tree like above
# intput_string =
# """
# 100, 1000, A # user_id, time_stamp, action
# 200, 1003, A
# 300, 1009, B
# 100, 1026, B
# 100, 1030, C
# 200, 1109, B
# 200, 1503, A"""
# # build the following tree
# """   
# |---A (2)
# |    |---B (2)
# |    |    |---C (1)
# |    |    |---A (1)
# |---B (1)
# """

def process(input_string):
    dic = collections.defaultdict(list)
    for line in input_string.split('\n'):
        line = line.replace(' ','')
        ele = line.split(',')
        dic[ele[0]].append((ele[1], ele[2]))
     return dic
intput_string = '100, 1000, A\n200, 1003, A\n300, 1009, B\n100, 1026, B\n100, 1030, C\n200, 1109, B\n200, 1503, A'
dat = process(intput_string)

class TrieNode:
    def __init__(self, char = "", count = 0) -> None:
        self.char = char
        self.child = {}
        self.count = count
        
root = TrieNode()

for _, elements in dat.items():
    sorted_elements = sorted(elements)
    print(sorted_elements)
    root_node = root
    for _, action in elements:
        if action not in root_node.child:
        root_node.child[action] = TrieNode(action, 1)
        else:
        root_node.child[action].count = root_node.child[action].count+1
        root_node = root_node.child[action]


"""
|--- A 2
|   |--- B 2
|   |   |--- C 1
|   |   |--- A 1
|--- B 1
"""

def printtree(prefix, root):
    
    if not root:
        print('\n')
      
    print(prefix, root.char, root.count)
    
    cnt = root.count
  
    for child in root.child:
        printtree('|   ' + prefix, root.child[child])
        cnt -= root.child[child].count
    # if cnt >= 0 and root.child:
    #     print('|   ' + prefix, 'dropoff', cnt)
    if root.count > 1 and cnt >= 0:
        print('|   ' + prefix, 'dropoff', cnt)
        
for child in root.child.keys():
    printtree('|---', root.child[child])
    

# // A -> [B,I,K]
# // B -> [A, D]
# // C -> [E]
# // D -> []
# // E -> []
# // F -> []
# // G -> [K]
# // I -> []
# // K -> []

# // Output - (A, B, D, I, G, K), (C, E), (F)

# Assume the input is a dict of list 

def dfs(dic):
    
    graph = collections.defaultdict(set)
    for key in dic.keys():
        for nei in dic[key]:
            graph[key].add(nei)
            graph[nei].add(key)
    
    ans = []    
    seen = set()
    
    for key in dic.keys():
        if key in seen: continue
        stack = [key]
        tmp = []
        while stack:
            node = stack.pop()
            if node in seen: continue
            seen.add(node)
            tmp.append(node)
            
            for target in graph[node]:
                if target in seen: continue
                stack.append(target)
                
        ans.append(tmp)
        
    return ans

dic = {}

parents = {key:key for key in dic.keys()}
rank = {key: 1 for key in dic.keys()}

def find(x):
    if x != parents[x]:
        parents[x] = find(parents[x])
    return parents[x]

def union(x, y):
    px, py = find(x), find(y)
    if px == py: return 0
    
    if rank[px] < rank[py]:
        parents[px] = py
    elif rank[py] < rank[px]:
        parents[py] = px
    else:
        parents[px] = py
        rank[py] += 1

for key in dic.keys():
    for target in dic[key]:
        print(parents)
        print(rank)
        print('===')
        union(key, target) 

result = collections.defaultdict(list)
for key in parents.keys():
    result[(parents[key])].append(key)
    
    
# 之后就是coding
# 给一个长度为n的unsorted array，可以找出有m个increasing elements的segments，然后把这m个segments merge成一个sorted array
# 其实就是merge k sorted array


arr = []
for _ in range(20):
    arr.append(random.randint(0, 100))
  
prev = -float('inf')

nums = []
tmp = []
for val in arr:
    if val > prev:
        tmp.append(val)
        prev = val
    else:
        nums.append(tmp)
        prev = val
        tmp = [val]
        
def mergeKLists(self, lists):
    """
    :type lists: List[ListNode]
    :rtype: ListNode
    """
    amount = len(lists)
    interval = 1
    while interval < amount:
        for i in range(0, amount - interval, interval * 2):
            lists[i] = self.merge2Lists(lists[i], lists[i + interval])
        interval *= 2
    return lists[0] if amount > 0 else None     
        
        

# 一个m*n的矩阵
# 0表示可走，1表示墙，求从a到b的最短路径
# BFS求解

def bfs(matrix, start, end):
    
    if not matrix:
        return None
    m, n = len(matrix), len(matrix[0])
    queue = collections.deque()
    queue.append((start, 0))
    seen = set()
    
    while queue:
        
        cur, depth = queue.popleft()
        
        if cur == end:
            return depth
        
        if cur in seen: continue
        
        seen.add(cur)
        i, j = cur
        for idx, idy in [(-1, 0), (1,0), (0, -1), (0, 1)]:
            if 0 <= i + idx < m and 0 <= j + idy < n and (i + idx, j + idy) not in seen and matrix[i + idx][j + idy] != 1:
                queue.append(((i + idx, j + idy), depth + 1))
        
    return None
        

# 给一个二维矩阵，0 代表wall，1 代表 road，大写字母代表 door，小写字母代表 key，然后给定一个初始点和重点坐标，求最短的路径的长度。时间不够，我就写了一个只有一个 door 的 solution，4 天后通知 rej。-ba

def bfs(matrix, start, end):
    
    if not matrix:
        return None
    
    m, n = len(matrix), len(matrix[0])
    
    queue = collections.deque()
    keys = [0]*26
    queue.append((start, tuple(keys)))
    seen = set((start, tuple(keys)))
    depth = 0
    
    while queue:
        
        n = len(queue)
        
        for _ in range(n):
            
            cur, key = queue.popleft()
            
            if cur == end:
                return depth
            
            # if (cur, key) in seen: continue
            # seen.add((cur, key))
    
            i, j = cur
            
            for idx, jdy in [(-1, 0), (1, 0), (0, 1), (0, -1)]:
                nx, ny, nkey = i + idx, j + jdy, list(key)
                
                if nx < 0 or nx >= m or ny < 0 or ny >= n or matrix[nx][ny] == 1: continue
                
                if matrix[nx][ny].isupper() and not nkey[ord(matrix[nx][ny]) - ord('A')]: continue
                
                if matrix[nx][ny].islower(): nkey[ord(matrix[nx][ny]) - ord('a')] = 1
                
                if ((nx, ny), tuple(nkey)) in seen: continue
                
                queue.append(((nx, ny), tuple(nkey)))
                seen.add(((nx, ny), tuple(nkey)))
            
        depth += 1
    
    return -1
                
                
# 2d array of 0,1,6 representing a maze that your character can walk through
# 0 - represents empty space, the character can walk over empty space
# 1 - represents a wall, the character cannot walk over a wall
# 6 - represents a monster, the character can walk over a monster if you choose to but it will lose a life

# a character that starts at position si, sj and tries to walk to ei, ej
# the character has N lives so it can walk over N-1 monsters
# the character is allowed to walk on the 4 neighboring cells‍‌‍‍‌‍‌‍‍‌‌‍‌‌‍‍‍‌‌‌ (up, down, left, right)

# return the shortest number of steps, -1 if impossible

# example grid

# g = [[0,1,0,0,0],
#      [0,6,0,1,0],
#      [0,0,0,1,0]]

# travel from 0,0 to 2,4
# 1 life  : shortest number of steps = 10
# 2 lives : shortest number of steps = 8


def shortestpath(grid, si, sj, ei, ej, k):
    
    m, n = len(grid), len(grid[0])
    
    queue = collections.deque()
    
    queue.append((si, sj, k))
    depth = 0
    seen = set((si, sj, k))
    
    while queue:
        
        l = len(queue)
        
        for _ in range(l):
            
            i, j, life = queue.popleft()
            
            if i == ei and j == ej: return depth
            
            for idx, jdy in [(-1, 0), (1, 0), (0, 1), (0, -1)]:
                nx, ny = i + idx, j + jdy
                
                if nx < 0 or nx >= m or ny < 0 or ny >= n or grid[nx][ny] == 1: continue
                
                if grid[nx][ny] == 6:
                    newlife = life - 1
                else:
                    newlife = life
                
                if newlife >= 1 and (nx, ny, newlife) not in seen:
                    queue.append((nx, ny, newlife))
                    seen.add((nx, ny, newlife))
                    
        depth += 1
        
    return -1
        


# 利口👂遛舅
# 但要求略有不同

# 要得到所有顺序而不是只有一种顺序。
# 参考这个，
# https://www.jianshu.com/p/467960b7d23c
# 这个是要多少种，所以用dp，面试官要求的是把顺序列出来，所以应该用dfs列举‍‌‍‍‌‍‌‍‍‌‌‍‌‌‍‍‍‌‌‌出来。写起来很复杂，最后没时间写完。


# original answer
import collections
class Solution:

    def alienOrder(self, words: List[str]) -> str:
        
        indegree = collections.defaultdict(int)
        outdege = collections.defaultdict(set)
        
        for word in words:
            for letter in word:
                indegree[letter] = 0
        
        for first, second in zip(words, words[1:]):
            for i, j in zip(first, second):
                if i != j:
                    if j not in outdege[i]:
                        indegree[j] += 1
                        outdege[i].add(j)
                    break
            else:
                if len(second) < len(first):
                    return ""
    
        stack = []
        
        for key in indegree.keys():
            if indegree[key] == 0:
                stack.append(key)
        result = []
        while stack:
            cur = stack.pop()
            result.append(cur)
            
            for target in outdege[cur]:
                indegree[target] -= 1
                if indegree[target] == 0:
                    stack.append(target)
        
        return "".join(result) if len(result) == len(indegree) else ""
    
    
# find all path 

class Solution:

    from collections import defaultdict, Counter, deque

    def alienOrder(self, words: List[str]) -> str:
        indegree = collections.defaultdict(int)
        outdege = collections.defaultdict(set)
        
        for word in words:
            for letter in word:
                indegree[letter] = 0
        
        for first, second in zip(words, words[1:]):
            for i, j in zip(first, second):
                if i != j:
                    if j not in outdege[i]:
                        indegree[j] += 1
                        outdege[i].add(j)
                    break
            else:
                if len(second) < len(first):
                    return ""
        
        stack = []
        
        for key in indegree.keys():
            if indegree[key] == 0:
                stack.append(key)
        
        track = set()
        perm = []
        ans = []

        
        def backtracking(stack, track, node):
            
            if len(track) == len(indegree):
                ans.append(''.join(perm[:]))
                return
                
            for key in stack:
                    if key in track: continue
                    track.add(key)
                    perm.append(key)
                    backtracking(stack + list(outdege[key]), track, outdege[key])
                    perm.pop()
                    track.remove(key)
            
        backtracking(stack, track, [])
        
        return ans

# just find the number

class Solution:

    from collections import defaultdict, Counter, deque

    def alienOrder(self, words: List[str]) -> str:
        indegree = collections.defaultdict(int)
        outdege = collections.defaultdict(set)
        
        for word in words:
            for letter in word:
                indegree[letter] = 0
        
        for first, second in zip(words, words[1:]):
            for i, j in zip(first, second):
                if i != j:
                    if j not in outdege[i]:
                        indegree[j] += 1
                        outdege[i].add(j)
                    break
            else:
                if len(second) < len(first):
                    return ""
        
        stack = []
        
        for key in indegree.keys():
            if indegree[key] == 0:
                stack.append(key)
                
        def dfs(root):
            
            if not outdege[root]:
                return 1
            
            res = 0
            
            for child in outdege[root]:
                res += dfs(child)
            
            return res + 1
        
# 扫雷 

nrow = 50
ncol = 50

mine = [[0]*nrow for _ in range(ncol)]
Nmine = 10
num=0
while num < Nmine:
    while True:
        i = random.randint(0, nrow - 1)
        j = random.randint(0, ncol - 1)
        if mine[i][j] != -1:
            mine[i][j] = -1
            break


for i in raneg(Nmine):
    x = i // nrow
    y = i % ncol
    mine[x][y] = -1
    
for i in range(ncol*nrow - 1, -1, -1):
    x = i // nrow
    y = i % ncol
    
    ind = random.randint(0, i)
    
    x_ind = ind // nrow
    y_ind = ind % ncol
    
    mine[x][y], mine[x_ind][y_ind] = mine[x_ind][y_ind], mine[x][y]

            

# Question: When are we all free?
# Context: OUr CEO wants to schedule an all-hands meeting.
# He wants to do it in a way, that doesn't disrupt employees' schedules.
# So he wants to find out when everyone is free at the same time.
# He also has in mind the earliest start time (ex. all hands cannot start before 9am)
# He also has in mind the latest end time (ex. all hands cannot end after 5pm)
# He has access to employees' schedules.

# In no particular format / encoding:
# schedules = {
#     "Alice": [(9:00am ~ 10am), (11:30am ~ 1:15pm), (3:00pm ~ 4:00pm)],
#     "Bob": [(9:45am ~ 10:15am), (1:15pm ~ 2:00pm)]
# }
# st‍‌‍‍‌‍‌‍‍‌‌‍‌‌‍‍‍‌‌‌art time: 8:30am
# end time: 5pm


# Output:
# [(8:30am ~ 9:00am), (10:15am ~ 11:30am), (2pm ~ 3:00pm), (4:00pm ~ 5:00pm)]

from datetime import datetime

out_time = datetime.strptime(m1, "%I:%M%p")
in_time = datetime.strptime(m2, "%I:%M%p")
'{:%I:%M%p}'.format(out_time)
interval = []

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
    

# Given two arrays, (say [1,3,5] and [2,4]) and a number target (say 7), assume we sort by the sum of any pair of elements from each array, return the smallest index.

# In this example, the result is 3.
# Pair, Sum, Index
# (1,2), 3, 0
# (1,4), 5, 1
# (3,2), 5, 2
# (3,4), 7, 3 <- result
# (5,2), 7, 4
# (5,4), 9, 5

class Solution:
    def kSmallestPairs(self, nums1: List[int], nums2: List[int], k: int) -> List[List[int]]:

        if k > len(nums1) * len(nums2):
            k = len(nums1) * len(nums2)
            
        heap = [[nums1[0] + nums2[0], 0, 0]]
        heapq.heapify(heap)
        ind = 0
        
        while heap and len(ans) < k:
            
            tol, i, j = heapq.heappop(heap)
            
            if tol == k:
                return ind
            
            if 0 <= i < len(nums1) and 0 <= j < len(nums2) - 1:
                heapq.heappush(heap, [nums1[i] + nums2[j+1], i, j + 1])
            
            if j == 0:
                if 0 <= i < len(nums1) - 1 and 0 <= j < len(nums2):
                    heapq.heappush(heap, [nums1[i+1] + nums2[0], i+1, 0])
            ind += 1
            
        return ind
    
# Hi, I was recently asked the following question: Given an input string which is the output of a count and say method, return the original number.

# For example: If the number if "21", then the count and say method would return
# "1211" (one two, one one). In this problem, the input provided to us is "1211" and our goal is to return "21".

# I answered this question by approaching it as a variant of the WordBreak problem with a dynamic programming solution. Of course, the conditions to check the validity of the split string will differ. Thoughts?

def reverse_count_say(num):
    original = ''
    num = str(num)
    for i in range(0, len(num), 2):
        a, b = num[i], num[i+1]
        current = int(a) * b
        original += current
    return original

list1 = ['a', 'b', 'c', 'd', 'ab', 'bc', 'cd', 'abc', 'bcd', 'abcd']

print(sorted(list1, key = lambda s: sum(map(ord, s)), reverse=True))