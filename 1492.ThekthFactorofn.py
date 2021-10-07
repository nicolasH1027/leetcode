class Solution:
    def kthFactor(self, n: int, k: int) -> int:
        
        factor = []
        sqrt = int(math.sqrt(n))
        for i in range(1, sqrt+1):
            if n % i == 0:
                k -= 1
                factor.append(i)
                if k == 0:
                    return i
        
        if sqrt*sqrt == n:
            k += 1
            
        n_fac = len(factor)
        
        return n // factor[n_fac - k] if k <= n_fac else -1
                
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