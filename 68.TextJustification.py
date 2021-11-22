def blank(n: int) -> str:
    return ' ' * n

class Solution:
    def fullJustify(self, words: List[str], maxWidth: int) -> List[str]:
        
        rpt, n = 0, len(words)
        ans = []
        
        while True:
            lpt = rpt
            sumLen = 0
            
            while rpt < n and sumLen + len(words[rpt]) + rpt - lpt <= maxWidth:
                sumLen += len(words[rpt])
                rpt += 1
            
            if rpt == n:
                s = ' '.join(words[lpt:])
                s += ' '*(maxWidth - len(s))
                ans.append(s)
                break
            
            numWords = rpt - lpt
            numSpaces = maxWidth - sumLen
            
            if numWords == 1:
                s = words[lpt] + ' '*numSpaces
                ans.append(s)
                continue
            
            avgSpace = numSpaces // (numWords - 1)
            extraSpace = numSpaces % (numWords - 1)
            
            s1 = ' '*(avgSpace + 1).join(words[lpt:lpt + extraSpace + 1])
            s2 = ' '*(avgSpace).join(words[lpt + extraSpace + 1: rpt])
            ans.append(s1 + ' '*avgSpace + s2)
        
        return ans