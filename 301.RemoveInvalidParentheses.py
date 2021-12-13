class Solution:
    def removeInvalidParentheses(self, s: str) -> List[str]:
        ans = []
        
        lr, rr = 0, 0
        
        for c in s:
            if c == '(':
                lr += 1
            elif c == ')':
                if lr != 0:
                    lr -= 1
                else:
                    rr += 1
                    
        def valid(s):
            cnt = 0
            for c in s:
                if c == '(':
                    cnt += 1
                elif c == ')':
                    cnt -= 1
                    if cnt < 0:
                        return False
            return cnt == 0
            
        def backtracking(s, start, lr, rr):
            if lr == 0 and rr == 0:
                if valid(s):
                    ans.append(s)
                return
            
            for i in range(start, len(s)):
                
                if i and s[i] == s[i-1]: continue
                
                if lr + rr > len(s) - i: return
                
                if lr and s[i] == '(':
                    backtracking(s[:i] + s[i+1:], i, lr-1, rr)
                if rr and s[i] == ')':
                    backtracking(s[:i] + s[i+1:], i, lr, rr-1)
        
        backtracking(s, 0, lr, rr)
        return ans                