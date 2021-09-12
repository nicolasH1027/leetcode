class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        "Recursion Version"
        if len(digits) == 0: 
            return []
        mapping = {
            "2": "abc", 
            "3": "def", 
            "4": "ghi", 
            "5": "jkl", 
            "6": "mno", 
            "7": "pqrs", 
            "8": "tuv", 
            "9": "wxyz"}
              
        def backtrack(ind, track):
            if len(track) == len(digits):
                result.append("".join(track))
                return
            letter = mapping[digits[ind]]
            for i in letter:
                track.append(i)
                backtrack(ind + 1, track)
                track.pop()
                
        result = []
        backtrack(0, [])
        return result
    

class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        "Iterative Version"
        if len(digits) == 0: 
            return []
        
        mapping = {
            "2": "abc", 
            "3": "def", 
            "4": "ghi", 
            "5": "jkl", 
            "6": "mno", 
            "7": "pqrs", 
            "8": "tuv", 
            "9": "wxyz"}
        
        queue = collections.deque(mapping[digits[0]])
        for i in range(1, len(digits)):
            tmp = []
            while queue:
                cur = queue.popleft()
                for letter in mapping[digits[i]]:
                    tmp.append(cur + letter) 
            queue = collections.deque(tmp)
        return queue
        
               
        