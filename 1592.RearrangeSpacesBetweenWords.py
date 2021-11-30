class Solution:
    def blank(self, num):
        return ' '*num
    
    def reorderSpaces(self, text: str) -> str:
        n = len(text)
        words = text.split()
        
        sumLen = 0
        for word in words:
            sumLen += len(word)
            
        numSpaces = n - sumLen
        
        if len(words) == 1:
            return words[0] + self.blank(numSpaces)
        
        avgSpace = numSpaces // (len(words) - 1)
        extraSpace = numSpaces % (len(words) - 1)
        
        if extraSpace == 0:
            return self.blank(avgSpace).join(words)
        else:
            return self.blank(avgSpace).join(words) + self.blank(extraSpace)