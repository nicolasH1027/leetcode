class Solution:
    def validWordAbbreviation(self, word: str, abbr: str) -> bool:
        
        i = 0
        j = 0
        n = len(abbr)
        m = len(word)
        count = 0
        while i < n:
            if abbr[i].isdigit():
                if abbr[i] == '0' and count == 0:
                    return False
                count = count * 10 + int(abbr[i])
            else:
                j += count
                if j >= m or abbr[i] != word[j]:
                    return False
                count = 0
                j += 1
            i += 1

        return j + count == m