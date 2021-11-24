class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        
        s = s.split()
        if len(pattern) != len(s):
            return False
        dic = {}
        
        for letter, word in zip(pattern, s):
            word += '!'
            if letter in dic:
                if dic[letter] != word:
                    return False
            if word in dic:
                if dic[word] != letter:
                    return False
            dic[letter] = word
            dic[word] = letter
            
        
        return True
    
class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        map_index = {}
        words = s.split()
        
        if len(pattern) != len(words):
            return False
        
        for i in range(len(words)):
            c = pattern[i]
            w = words[i]

            char_key = 'char_{}'.format(c)
            char_word = 'word_{}'.format(w)
            
            if char_key not in map_index:
                map_index[char_key] = i
            
            if char_word not in map_index:
                map_index[char_word] = i 
            
            if map_index[char_key] != map_index[char_word]:
                return False
        
        return True
    
class Solution:
    def wordPattern(self, pattern, str):
        s = pattern
        t = str.split()
        return len(set(zip(s, t))) == len(set(s)) == len(set(t)) and len(s) == len(t)