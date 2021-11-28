class Solution:
    def isNumber(self, s: str) -> bool:
        
        met_dig = met_exp = met_dot = False
        
        for i, c in enumerate(s):
            
            if c == '+' or c =='-':
                if i > 0 and s[i-1] != 'e' and s[i-1] != 'E':
                    return False
                met_exp = False
                met_dig = False
            
            elif c == 'e' or c == 'E':
                if met_exp or not met_dig:
                    return False
                met_dig = False
                met_exp = True
            
            elif c == '.':
                if met_dot or met_exp:
                    return False
                met_dot = True
            
            elif c.isdigit():
                met_dig = True
            
            else:
                return False
        
        return met_dig