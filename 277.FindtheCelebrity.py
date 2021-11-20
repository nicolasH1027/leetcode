# The knows API is already defined for you.
# return a bool, whether a knows b
# def knows(a: int, b: int) -> bool:

class Solution:
    def findCelebrity(self, n: int) -> int:
        
        target = 0

        for i in range(1, n):
            if knows(target, i):
                target = i
            
        for i in range(n):
            if not knows(i, target):
                return -1
            
        for i in range(n):
            if knows(target, i) and i != target:
                return -1
            
        return target