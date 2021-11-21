class Solution:
    def countOfAtoms(self, formula: str) -> str:
        n = len(formula)
        stack = []
        dic = {}
        i = 0
        
        while i < n:
            
            c = formula[i]
            
            if c == "(" or c == ")":
                stack.append(c)
                i += 1
            else:
                if c.isdigit():
                    j = i
                    while j < n and formula[j].isdigit():
                        j += 1
                    cnt = int(formula[i:j])
                    i = j
                    
                    if stack and stack[-1] == ")":
                        tmp = []
                        stack.pop()
                        
                        while stack and stack[-1] != "(":
                            cur = stack.pop()
                            dic[cur] = dic.get(cur, 1)*cnt
                            tmp.append(cur)
                        stack.pop()
                        
                        for item in tmp:
                            stack.append(item)
                    else:
                        cur = stack.pop()
                        dic[cur] = dic.get(cur, 1)*cnt
                        stack.append(cur)
                else:
                    j = i + 1
                    while j < n and formula[j].islower():
                        j += 1
                    cur = formula[i:j] + '.' + str(i)
                    dic[cur] = 1
                    i = j
                    stack.append(cur)
        
        merge_dic = {}
        
        for key, val in dic.items():
            cur = key.split('.')[0]
            merge_dic[cur] =  merge_dic.get(cur, 0) + val
        
        res = []
        for key in sorted(merge_dic.keys()):
            if  merge_dic[key] > 1:
                res.append(key + str(merge_dic[key]))
            else:
                res.append(key)
                
        return "".join(res)    
            
        