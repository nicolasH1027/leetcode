class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        
        if not s:
            return True
        
        if not t or len(s) > len(t):
            return False
        
        n1 = len(t)
        n2 = len(s)
        i = 0
        j = 0
        
        while i < n1 and j < n2:
            
            if t[i] == s[j]:
                j += 1
            
            i += 1
        
        return j == len(s)
    

class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        
        dic = collections.defaultdict(list)
        
        for ind, c in enumerate(t):
            dic[c].append(ind)
        
        cur_ind = -1
        
        for c in s:
            
            if c not in dic:
                return False
            
            ind_list = dic[c]
            
            s_ind = bisect.bisect_right(ind_list, cur_ind)
            
            if s_ind != len(ind_list):
                cur_ind = ind_list[s_ind]
            else:
                return False
        
        return True