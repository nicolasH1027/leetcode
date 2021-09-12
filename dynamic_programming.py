# rod cutting problem


from math import inf
price = [1, 5, 8, 9, 10, 17, 17, 20, 24, 30]


# recursion implementation
def MaxValueCut(n, price):
    "Recursive implementaion"
    revenue = [float(-inf) for i in range(n + 1)]
    def helper(n, price, revenue):    
        if revenue[n] >= 0:
            return revenue[n]
        if n == 0:
            p = 0
        else:
            p = float(-inf)
            for i in range(n):
                p = max(p, price[i] + helper(n - i - 1, price, revenue))        
        revenue[n] = p
        return p
    helper(n, price, revenue)
    return revenue
        
# iterative implementation

def MaxValueCutIte(n, price):
    revenue = [0]*(n + 1)
    for j in range(1, n + 1):
        q = float(-inf)
        for i in range(1, j + 1):
            q = max(q, revenue[j - i])
        revenue[j] = q
    
    return revenue



# matrix chain product


")()())"

def validparen(s):
    
    state = 0
    
    for i in s:
        if i == "(":
            state += 1
        
        else: 
            state -= 1
            if state < 0:
                return False
    
    return True if state == 0 else False


                
    
    
    
