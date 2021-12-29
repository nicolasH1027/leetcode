class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        if num1 == '0' or num2 == '0':
            return '0'
        
        ans, n, m = '0', len(num1), len(num2)
        
        for i in range(m - 1, -1, -1):
            y, carry = int(num2[i]), 0
            cur = collections.deque(['0']*(m - i - 1))
            for j in range(n - 1, -1, -1):
                carry, digit = divmod(int(num1[j])*y + carry, 10)
                cur.appendleft(str(digit))
            if carry:
                cur.appendledft(str(carry))
            ans = self.add(ans, ''.join(cur))
        
        return ''.join(ans)

    def add(self, num1: str, num2: str):
        
        n = max(len(num1), len(num2))
        ans, carry, num1, num2 = collections.deque(), 0, num1.zfill(n), num2.zfill(n)
        
        for i in range(n-1, -1, -1):
            
            carry, digit = divmod(ord(num1[i]) + ord(num2[i]) - 2*ord('0') + carry, 10)
            
            ans.appendleft(str(digit))
        
        if carry:
            ans.appendleft('1')
        
        return ''.join(ans)


class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        if num1 == '0' or num2 == '0':
            return '0'
        
        m, n = len(num1), len(num2)
        ans = [0]*(m+n)
        
        for i in range(m-1, -1, -1):
            x = int(num1[i])
            for j in range(n-1, -1, -1):
                ans[i + j + 1] += x*int(num2[j])
                
        for i in range(m+n-1, 0, -1):
            ans[i-1] += ans[i] // 10
            ans[i] %= 10
            
        ind = 0 if ans[0] else 1
        
        return ''.join(str(x) for x in ans[ind:])