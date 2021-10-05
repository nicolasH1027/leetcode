class Solution:
    def isAlienSorted(self, words: List[str], order: str) -> bool:
        mapping = {}
        for i, ch in enumerate(order):
            mapping.setdefault(ch, i)
        
        for i in range(len(words) - 1):
            
            for first, second in zip(words[i], words[i+1]):
                if mapping[first] != mapping[second]:
                    if  mapping[first] > mapping[second]:
                        return False
                    break
            else:
                if len(words[i]) > len(words[i+1]):
                    return False
        return True
    