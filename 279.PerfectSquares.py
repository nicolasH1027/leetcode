from math import inf


class Solution:
    def numSquares(self, n: int) -> int:
        "Backtracking, brute force, TLE"
        def backtrack(n):
            if n == 0:
                return 0
            count = inf
            i = 1
            while i*i <= n:
                count = min(count, backtrack(n - i*i) +  1)
                i += 1
            return count   
        return backtrack(n)
                
                
class Solution:
    def numSquares(self, n: int) -> int:
        "Backtracking, with memorization, AC"
        seen = {}
        def backtrack(n, seen):
            if n in seen:
                return seen[n]
            if n == 0:
                return 0
            count = inf
            i = 1
            while i*i <= n:
                count = min(count, backtrack(n - i*i, seen) + 1)
                i += 1
            seen[n] = count
            return count
        return backtrack(n, seen)
        
# the memorization recursion is the same with dynamic programming
# check the rod cutting problem
              
class Solution:
    def numSquares(self, n: int) -> int:
        "dynamic programming"
        dp = [inf]*(n + 1)
        dp[0] = 0  
        for i in range(1, n + 1):
            j = 1
            while j*j <= i:
                dp[i] = min(dp[i], dp[i - j*j] + 1 ) 
                j += 1        
        return dp[n]
    

# BFS idea 
# N-ary tree

class Solution:
    def numSquares(self, n: int) -> int:
        "Recursion Version"
        square_list = [i**2 for i in range(1, int(math.sqrt(n)+1))] 
        def is_valid(n, count): 
            if count == 1:
                return True if n in square_list else False  
            for s in square_list:
                return is_valid(n - s, count - 1)
            return False
            
        for i in range(1, n + 1):
            if is_valid(n, i):
                return i

# time complexity is n^(h) h is the height of the N-ary Tree

class Solution:
    def numSquares(self, n: int) -> int:
        "Iterative Version"
        square_list = [i**2 for i in range(1, int(math.sqrt(n)+1))] 
        
        queue = set()
        queue.add(n)
        level = 0
        while queue:
            level += 1
            new_queue = set()
            for item in queue:
                for s in square_list:
                    if item == s:
                        return level
                    elif item < s:
                        break
                    else:
                        new_queue.add(item - s)    
            queue = new_queue
        return level

            
        