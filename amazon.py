"249. Group Shifted Strings"

class Solution:
    def groupStrings(self, strings: List[str]) -> List[List[str]]:
        """
        The difference between each character in the string
        characterize the group pattern
        """
        
        def decode(s):
            n = len(s)
            ans = ''
            for i in range(n - 1):
                tmp = ord(s[i]) - ord(s[i+1])
                if tmp < 0:
                    tmp += 26
                ans += str(tmp)
            return ans
        
        mapping = collections.defaultdict(list)
        
        for s in strings:
            token = decode(s)
            mapping[token].append(s)
            
        return mapping.values()

"1492. The kth Factor of n"
class Solution:
    def kthFactor(self, n: int, k: int) -> int:
        
        factor = []
        sqrt = int(math.sqrt(n))
        for i in range(1, sqrt+1):
            if n % i == 0:
                factor.append(i)
                if len(factor) == k:
                    return i
        
        n_tol = 2*len(factor)
        if sqrt*sqrt == n:
            k += 1
        
        return n // factor[n_tol - k] if k <= n_tol else -1
        
"1328. Break a Palindrome"
class Solution:
    def breakPalindrome(self, palindrome: str) -> str:
        n = len(palindrome)
        if n == 1:
            return ""
        
        for i in range( n // 2):
            if palindrome[i] != 'a':
                return palindrome[:i] + 'a' +  palindrome[i+1:]
        
        return palindrome[:-1] + 'b'
            
"2. Add Two Numbers"

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        
        dummy = ListNode()
        prev = dummy
        carry = 0
        
        while True:
            
            x = l1.val if l1 else 0
            y = l2.val if l2 else 0
            
            val, carry = divmod(x + y + carry, 10)
            tmp = ListNode(val)
            prev.next = tmp
            prev = tmp
            
            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None
            
            if not l1 and not l2 and not carry:
                break
            
        return dummy.next
    

"""
common prefix length

aaaaa aaaaa, 5
aaaaa aaaa, 4
aaaaa aaa, 3
aaaaa aa, 2
aaaaa a, 1

所以总匹配树为15
"""

"naive way"
def ComputeZ(s):
    n = len(s)
    z = [0]*n
    for i in range(1, n):
        while i + z[i] < n and s[z[i]] == s[i + z[i]]:
            z[i] += 1    
    return z

"""
超过本人解释能力

只能说这个[l, r]类似于kmp里面next数组的作用，减少比较次数
看这个吧 https://www.zhihu.com/column/c_1182444932760125440
"""
def Z_algorithm(s):
    n = len(s)
    z = [0] * n
    l = r = 0

    for i in range(1, n):
        if i <= r:
            z[i] = min(r - i + 1, z[i - l])
        while i + z[i] < n and s[z[i]] == s[i + z[i]]:
            z[i] += 1
        if i + z[i] - 1 > r:
            l, r = i, i + z[i] - 1

    return n + sum(z)

"""
上面是吧后缀和原string进行对比，

下面这个是吧后缀和前缀进行对比
"""
def Z_algorithm(s):
    n = len(s)
    z = [0] * n
    l = r = 0

    for i in range(1, n):
        if i <= r:
            z[i] = min(r - i + 1, z[i - l])
        while i + z[i] < n and s[z[i]] == s[i + z[i]]:
            z[i] += 1
        if i + z[i] - 1 > r:
            l, r = i, i + z[i] - 1
    for i in range(1, n):
        z[i] = min(z[i], i)
    return n + sum(z) # 要不要加n需要和面试官沟通

"""
'ABA'

password strength, distinct character, 2

AND

828. Count Unique Characters of All Substrings of a Given String, 1

"""

"两道题的思路都一样，与其找substring，直接看每一个字母的贡献度"

# 828. Count Unique Characters of All Substrings of a Given String, 1
class Solution:
    def uniqueLetterString(self, s: str) -> int:
        
        """
        假设 'A' 出现在 index 3 和 index 6的位置
        那么对于起点从0到3的字符以及结尾是3 4 5 的字符，A
        都只unique的，所以贡献 4*3 = 12 次
        """
        pos, ans, n = collections.defaultdict(list), 0, len(s)
        for i, c in enumerate(s):
            pos[c].append(i)
        
        for key in pos.keys():
            tmp = [-1] + pos[key] + [n]
            for i in range(1, len(tmp) - 1):
                ans += (tmp[i-1]-tmp[i])*(tmp[i+1]-tmp[i])
        return ans % (10**9 + 7)
    
"上述算法的空间可以压缩到常数级别"
class Solution:
    def uniqueLetterString(self, s: str) -> int:
        pos, ans, n = {c:[-1,-1] for c in s}, 0, len(s)
        
        for i, c in enumerate(s):
            lag2, lag1 = pos[c]
            ans += (lag1 - lag2) * (i - lag1)
            pos[c] = [lag1, i]
            
        for c in pos.keys():
            lag2, lag1 = pos[c]
            ans += (n - lag1)*(lag1 - lag2)

        return ans % (10**9 + 7)
    
"password strength, distinct character"

def strength(s):        
    """
    这题其实是一样的，但是这题求的是number of distinct letter，区别就是
    假设我们求 ‘A’， 那么我们只需要知道A第一次出现的substring，之后再出现，他都是
    贡献1。具体实现看代码
    """
    pos = {chr(97+i): -1 for i in range(26)} # 题目限定是26个字母
    ans, n = 0, len(s)
    
    for i, c in enumerate(s):
        ans += (i - pos[c])*(n - i)
        pos[c] = i
    
    return ans



"""
金属棒工厂的厂长拥有 n 根多余的金属棒。当地的一个承包商提出，只要所有的棒材具有相同的长度（用 saleLength 表示棒材的长度），就将金属棒工厂的剩余棒材全部购买。厂长可以通过将每根棒材切割零次或多次来增加可销售的棒材数量，但是每次切割都会产生一定的成本（用 costPerCut 表示每次切割的成本）。等所有的切割完成以后，多余的棒材将被丢弃，没有利润。金属棒工厂的厂长获得的销售总利润计算公式如下：

totalProfit = totalUniformRods * saleLength * salePrice - totalCuts * costPerCut

其中 totalUniformRods 是可销售的金属棒数量，salePrice 是承包商同意支付的每单位长度价格，totalCuts是需要切割棒材的次数。

https://www.jiuzhang.com/solution/cutting-metal-surplus/?utm_source=sc-tianchi-sz-0412
"""

class Solution:
    """
    @param costPerCut: integer cost to make a cut 
    @param salePrice: integer per unit length sales price 
    @param lengths: an array of integer rod lengths 
    @return: The function must return an integer that denotes the maximum possible profit. 
    """
    def maxProfit(self, costPerCut, salePrice, lengths):
        profit, max_len = 0, 0
        for length in lengths:
            max_len = max(max_len, length)
            
        for i in range(1, max_len + 1):
            cut, pieces = 0, 0
            for length in lengths:
                cur_cut = (length - 1) // i
                cur_piece = length // i
                if i * salePrice * cur_piece - costPerCut * cur_cut > 0:
                    cut += cur_cut
                    pieces += cur_piece
                    
            profit = max(profit, i * salePrice * pieces - costPerCut * cut)
        
        return profit
    

"1099. Two Sum Less Than K"

class Solution:
    def twoSumLessThanK(self, nums: List[int], k: int) -> int:
        nums.sort()
        l, r = 0, len(nums) - 1 
        ans = -float('inf')
        while l < r:
            tol = nums[r] + nums[l]
            if tol >= k:
                r -= 1
            else:
                ans = max(ans, tol)
                l += 1
        return ans if ans != -float('inf') else -1

class Solution:
    def twoSumLessThanK(self, nums: List[int], k: int) -> int:
        "linear solution"
        answer = -1
        count = [0] * 1001
        for num in nums:
            count[num] += 1
        lo = 1
        hi = 1000
        while lo <= hi:
            if lo + hi >= k or count[hi] == 0:
                hi -= 1
            else:
                if count[lo] > (0 if lo < hi else 1):
                    answer = max(answer, lo + hi)
                lo += 1
        return answer
    

"881. Boats to Save People"

class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        
        people.sort()
        l, r, cnt = 0, len(people) - 1, 0
        while l <= r:
            tol = people[r] + people[l]
            if tol <= limit:
                l += 1
            r -= 1
            cnt += 1
        return cnt
    
    
"Lintcode 1338 · Parking Dilemma"

"""
There are many cars parked in the parking lot. The parking is a straight very long line and a parking slot for every single meter. There are cars parked currently and you want to cover them from the rain by building a roof. The requirement is that at least k cars are covered by the roof.What's the minium length of the roof that would cover k cars?
The function has the following parameters:

cars: integer array of length denoting the parking slots where cars are parked
k: integer denoting the number of cars that have to be covered by the roof
"""

class Solution:
    """
    @param cars:  integer array of length denoting the parking slots where cars are parked
    @param k: integer denoting the number of cars that have to be covered by the roof
    @return: return the minium length of the roof that would cover k cars
    """
    def ParkingDilemma(self, cars, k):
        cars.sort()
        ans = float('inf')
        for i in range(k-1, len(cars)):
            ans = min(ans, cars[i] - cars[i - k + 1] + 1)
        return ans


"""
An Amazon seller is celebrating ten years in business! They are having a sale to honor their privileged members, those who have purchased from them in the past five years. These members receive the best discount indicated by any discount tags attached to the product. Determine the minimum cost to purchase all products listed. As each potential price is calculated, round it to the nearest integer before adding it to the total. Return the cost to purchase all items as an integer.

There are three types of discount tags:

Type 0: discounted prifce, the item is sold for a given price.
Type 1: percentage discount, the customer is given is fixed percentage discount from the retail price.
Type 2: fixed discount, the customer is given a fixed amount off from the retail price.

Input
products: an [n][m] 2D array of product descriptors as strings: price followed by m-1 discount tags
discounts: an [d][3] 2D array of tag descriptors as strings: tag, type, amount
Output
the total amount paid for all listed products, discounted to privileged members' pricing

Examples
Example 1:
Input:

products = [['10', 'do', 'd1'], ['15', 'EMPTY', 'EMPTY'], ['20', 'd1', 'EMPTY']]
discounts = [['d0','1','27'], ['d1', '2', '5']]
Output: 35
"""

dic = {}

for tag, type, num in discounts:
    dic[tag] = (type, num)

for item in products:
    price, tag1, tag2 = item
    

# just iterate all product and find the minimum






"""
An e-commerce company imports a type of fitness band from China and sell them in the US for a higher price. The company source the product from multiple suppliers, each with their own inventory. The suppliers raise the price of their product when inventory decreases due to scarcity. More specifically, the profit that the e-commerce company makes on each product sold is equal to the number of products left from the supplier.

Given a list of integers representing the number of products each supplier has and an integer representing the number of products sold, find the maximum profit the company can make.

Examples
Example 1:
Input:
inventories = [6, 4] order = 4

Output: 19
Explanation:
There are two suppliers, with inventory of 4 and 6 respectively. A total of 4 items are ordered. We can make maximum profit by

selling 1 item from the first supplier for 6
selling 1 item from the first supplier for 5
selling 1 item from the first supplier for 4, which brings down the inventory of the first supplier to 3
selling 1 item from the second supplier for 4
The maximum profit is 6 + 5 + 4 + 4 = 19.

Example 2:
Input:
inventories = [10, 10]

order = 5

Output: 46
Explanation:
The maximum profit we can generate is by

selling 1 item for a profit of 10 from the first supplier
selling 1 item for a profit of 10 from the second supplier
selling 1 item for a profit of 9 from the first supplier
selling 1 item for a profit of 9 from the second supplier
selling 1 item for a profit of 8 from the first or second supplier
The maximum profit is 10 + 10 + 9 + 9 + 8 = 46.
"""
"1648. Sell Diminishing-Valued Colored Balls"


class Solution:
    def maxProfit(self, inventory: List[int], orders: int) -> int:
        "the space can be optimized into O(1), by directly sort the orginal arr"
        def SerSum(lo, hi):
            return (lo + hi)*(hi - lo + 1) // 2
        
        stock = sorted(collections.Counter(inventory).items(), reverse = True)
        
        CuSum, n, colors = 0, len(stock), 0
        
        for i, (CurPrice, num) in enumerate(stock):
            
            if orders <= 0:
                break
            
            "找到下一个价格"
            NextPrice = stock[i+1][0] if i < n - 1 else 0
            
            "计算现在一共有多少个供应商或者是球的颜色的种类"
            colors += num
            
            "一共能提供多少offer"
            NumBall = colors*(CurPrice - NextPrice)
            
            "在orders和NumBall 中取一个小的， 然后divmod， 商就是我们还需要降低多少价格， 余数就是不能够完全把已有供应商的货品卖到下一个价格的水平"
            full, part = divmod(min(NumBall, orders), colors)
            CuSum += (SerSum(CurPrice - full+1, CurPrice)*colors + (CurPrice - full) * part) % (10**9 + 7)
            orders -= NumBall
        
        return CuSum % (10**9 + 7)



"435. Non-overlapping Intervals"
"""
求最少需要去除几个区间才能让剩余的non-overlap, 那么我们求不去除
任何区间的情况下，最多有几个不重叠区间，最后区间总数减去做多几个不重叠的，
就是我们要求的树
"""
class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        
        intervals.sort(key = lambda x: x[1])
        
        cnt = 0
        prev = -float('inf')
        for item in intervals:
            if item[0] >= prev:
                cnt += 1
                prev = item[1]
        return len(intervals) - cnt
    
    
"696. Count Binary Substrings"

class Solution:
    def countBinarySubstrings(self, s: str) -> int:
        count, prev, cur = 0, 0, 1
        for i in range(len(s) - 1):
            if s[i] != s[i+1]:
                count += min(cur, prev)
                prev, cur = cur, 1
            else:
                cur += 1     
        return count + min(prev, cur)


"""
Consider a string consisting of lowercase English alphabetic letters (i.e., [a-z]) only. We use the following rules to encode all of its characters into string s:
· a is encoded as 1, b is encoded as 2, c is encoded as 3, ..., and i is encoded as 9.
· j is encoded as 10#, k is encoded as 11#, i is encoded as 12#, ..., and z is encoded as 26#.
· If there are two or more consecutive occurrences of any character, then the character count is written within parentheses (i.e., (c) , where c is an integer denoting the count of consecutive occurrences being encoded) immediately following the character. For example, consider the following string encodings:
o String "abzx" is encoded as s = "1226#24#".
o String "aabccc" is encoded as s = "1(2)23(3)".
o String "bajj" is encoded as s = "2110#(2)".
o String "wwxyzwww" is encoded as s = "23#(2)24#25#26#23#(3)°.
Complete the frequency function in the editor below. It has one parameter: a string, s, that was encoded using the rules above and consists of digits (i.e., decimal integers from 0 to 9), # symbols, and parentheses. It must return an array of 26 integ
· The element at index 0 denotes the frequency of character a in the original string.
· The element at index 1 denotes the frequency of character b in the original string.
· The element at index 2 denotes the frequency of character c in the original string.
· The element at index 25 denotes the frequency of character z in the original string. Input Format
Locked stub code in the editor reads encoded string s from stdin and passes it to the function.
Constraints
· String s consists of decimal integers from 0 to 9, #s, and O's only.
· 1 length of s 105
· It is guaranteed that string s is a valid encoded string.
· 2 c 104, where c is a parenthetical count of consecutive occurrences of an encoded character.
Output Format
The function must return an array of 26 integers denoting the respective frequencies of each character (i.e., a through z) in the decoded string. This is printed to stdout by locked stub code in the editor.
Sample Input 0
1226#24#
Sample Output 0
1 1 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 1 0 1
"""

def decode(s):
    pt, n, stack = 0, len(s), []
    ans = [0]*26
    while pt < n:
        if s[pt] == ')':
            num, expo = 0, 0
            while stack[-1] != '(':
                num += int(stack.pop())*10**expo
                expo += 1
            stack.pop()
            ans[int(stack.pop()) - 1] += num
        elif s[pt] == '#':
            tmp = ''
            tmp += stack.pop()
            tmp += stack.pop()
            stack.append(tmp[::-1])
        else:
            stack.append(s[pt])
        pt += 1
    while stack:
        ans[int(stack.pop()) - 1] += 1
    return ans
        
"""
Hi,

I got Amazon questions countMaximumTeams. Given an skill array example - [3,4,3,1,6,5] and teamSize = 3 and maxDiff =2.
public int countMaximumTeams(List skill,int teamSize, int maxDiff)

Target: So, Try to form maximum teams size 3 each, e.g., here 2 team1 = [3,3,1] ( As max skill (3) differ from min. skill(1)=3-1 = 2) - so this is valid combination. Other team2 = [4,6,5] (as max skill(6) - min.skill(4)=2) - so this one is valid too. Maximum two combination or teams can be form

Output: 2
"""
            
def find(arr, teamSize, maxDiff):   

    arr.sort()

    i, answer = 0, 0
    while (i <= (len(arr)-teamSize)):    
        if(arr[i+teamSize-1] - arr[i] <= maxDiff):
            answer += 1
            i += teamSize
        else:
            i += 1    
    return answer




"""Your team at on has been asked to help outline options for a hypothetical investment strategy. Imagine an investor opens a new account and wants to investnumber of assets. 
Each asset begins with balance of 0, and its value is stored in an array using 1-based indexing. Periodically, a contribution is received and equal investments are made in a subset of the portfolio. 
Each contribution will be given by investment amount, start index, end index. 
Each investment in that range will receive the contribution amount. Determine the maximum amount invested in any one investment after all contributions.

Input:

n = 5
rounds = [[1, 2, 10], [2, 4, 5], [3, 5, 12]]
Output: 17
"""

def findmax(n, rounds):
    "前缀和简单应用"
    presum = [0]*n
    
    for l, r, val in rounds:
        presum[l-1] += val
        presum[r] -= val
    
    for i in range(1, n):
        presum[i] += presum[i-1]
    
    return max(presum)

"""
You've been nominated to participate in a programming challenge as part of your Day 1 Orientation at Amazon. 
Given an array of bad numbers and a range of integers, determine the longest segment of integers within the range that does not include any bad numbers.

Input:

bad_numbers = [37,7,22,15,49,60]
lower = 3
upper = 48
Output: 14
"""

def segment(arr, left, right):
    "这种一看，排序跑不掉，TC nlogn"
    arr.sort()
    "去除在区间范围右侧的点"
    while arr and arr[-1] > right:
        arr.pop()
    
    "加入这个点的意义是为了解决右边界上的问题"
    arr.append(right + 1)
    "从 left-1 开始是为了解决左边界的问题"
    lo, ans = left-1, 0
    for num in arr:
        if num < lo: continue # 解决数组存在范围左侧的点
        ans = max(ans, num - lo - 1)
        lo = num
    return ans

        
        
"""
Given an array of integers, determine the number of ways the entire array be split into two non-empty subarrays, left and right, 
such that the sum of elements in the left subarray is greater than the sum of elements in the right subarray.

Example

arr =  [10, 4, -8, 7]

There are three ways to split it into two non-empty subarrays:


  
[10] and [4, -8, 7], left sum = 10, right sum = 3

  
[10, 4] and [-8, 7], left sum = 10 + 4 = 14, right sum = -8 + 7 = -1

  
[10, 4, -8] and [7], left sum = 6, right sum = 7

The first two satisfy the condition that left sum > right sum, so the return value should be 2.
"""

def findways(arr):
    "easy, 前缀和"
    n = len(arr)
    for i in range(1, n):
        arr[i] += arr[i-1]
    cnt, tol = 0, arr[-1]
    for i in range(n-1):
        if arr[i] > tol - arr[i]:
            cnt += 1
    return cnt


"""
You are given a List of Integers which is a list of priorities. A priority can be a number from 1-99. 
Without changing the order of the array, minimize the priority as much as possible without changing the order.

Example

arr = [1, 4, 8, 4]

->

[1, 2, 3, 2]
"""

def lowerpriority(arr):
    "灵感来自于sample exclude blacklist, 需要一个mapping把值往前面map"
    pt, mapping = 1, {val:1 for val in arr}

    for i in range(1, 100):
        if  mapping.get(i, 0):
            mapping[i] = pt
            pt += 1
    
    for i, val in enumerate(arr):
        arr[i] = mapping[val]
    
    return arr
    
    
"""
An Amazon seller is deciding which of their products to invest in for the next quarter to maximize their profits. 
They have each of their products listed as segments of a circle. Due to varying market conditions, the products do not sell consistently. 
The seller wants to achieve maximum profit using limited resources for investment. 
The product list is segmented into a number of equal segments, and a projected profit is calculated for each segment. 
The projected profit is the cost to invest versus the sale price of the product. 
The seller has chosen to invest in a number of contiguous segments along with those opposite. 
Determine the maximum profit the seller can achieve using this approach.

For example, the product list Is divided into n = 6 sections and will select k = 2 contiguous sections and those opposite to invest in. 
The profit estimates are profit = [1, 5, 1, 3, 7, -3] respectively. 
The diagrams below show the possible choices with profits[0] at the 9 o'clock position and filling counterclockwise.

The profit levels, from left to right, are 1+5+7+3=16, 5+1+7+-3=10, and 1+3+-3+1=2. The maximum profit is 16.

Input
k: an integer that denotes half of the needed number of products within the list
profit: an array of integers that denote the profit from investing in each of the products
Output
the maximum profit possible

Examples
Example 1:
Input:

k = 2
profit = [1, 5, 1, 3, 7 -3]
Output: 16

Explanation:

The profit levels, from left to right, are 1+5+7+3=16, 5+1+7+-3=10, and 1+3+-3+1=2. The maximum profit is 16.

Example 2:
Input:

k = 1
profit = 3 -5
Output: -2

Explanation:

Here k=1 and n=2. The seller will choose 2*k=2 products. In this case, it is the entire list, so overall profit is 3+-5=-2.


-we will traverse through the array from index 1 to index n-1
-each iteration we will add the price of the pair at index (i+k-1)%n and subtract the pair at index i-1 to get a new sum
-then we compare that new sum to the max_sum
"""
    
def MaxProfit(arr, k):
    
    max_profit, n = 0, len(arr) // 2

    for i in range(k):
        max_profit += arr[i] + arr[n + i]
    cur = max_profit
    for i in range(1, n):
        cur += arr[(i+k-1) % n] + arr[(i+k-1)%n + n] - arr[i+n-1] - arr[i-1]
        max_profit = max(max_profit, cur)
    
    return max_profit

"""
. 学生根据兴趣选课的情景，其实就是input是一个有-1，和1的array，[-1, -1, 1, -1] 这样的，
让求product为positive的max length，这个题之前地里有人发过，思路就是找出第一个和最后一个-1的位置，
同时count一下有多少个-1，如果是偶数个，直接返回整个array length，
如果是奇数个，就舍弃第一个-1之前的或者舍弃最后一个-1之后的，求一下max
"""

"""
2. 情景是给一个list of coupons让判断每个coupon是否valid，就是decode string那个题套个场景，
string valid的要求是xYx的形式，就是abba或者aba这种。这个大家之前也说过，
就是用stack来记录之前见过的char，如果curr char和stack上的不一样就push，
如果一样就pop，最后检查stack是不是为空
"""