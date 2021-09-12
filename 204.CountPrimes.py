class Solution:
    def countPrimes(self, n: int) -> int:
        "nlog(logn)"
        if n <= 2:
            return 0
        seen = set()
        for i in range(2, int(math.sqrt(n)) + 1):
            if i not in seen:
                for multiple in range(i*i, n, i):
                    seen.add(multiple)
        return n - len(seen) - 2

class Solution: 
    "faster implementation"
    def countPrimes(self, n):
        if n <= 2:
            return 0
        primes = [1] * n
        primes[0] = primes[1] = 0
        for i in range(2,  int(math.sqrt(n)) + 1):
            if primes[i]:
                for j in range(i*i, n, i):
                    primes[j] = 0
        return sum(primes)