class Solution:
    def isHappy(self, n: int) -> bool:
        seen = set()
        seen.add(n)
        while True:
            result = 0
            while n != 0:
                n, rem = divmod(n, 10)
                result += rem**2  
            if result == 1 or result in seen:
                break
            seen.add(result)
            n = result
        return result == 1