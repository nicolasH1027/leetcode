class Solution:
    def findSubstring(self, s: str, words: List[str]) -> List[int]:

        ans, n, k, l = [], len(s), len(words), len(words[0])
        
        need = {}
        
        for word in words:
            need[word] = need.get(word, 0) + 1
        
        """
        Because the length of each word in words are the same, so we dont need to iterate
        every word in s one by one, instead, we only need to check different combination of k*l
        in s,  start from 0 to l 
        """
        for i in range(l):
            "cnt store how many needed words we encounter"
            left, cnt, valid = i, 0, {}
            
            for j in range(i, n - l + 1, l):
                
                sub = s[j:j+l]
                
                "not the word needed, reset everything"
                if sub not in need:
                    
                    valid.clear()
                    
                    cnt = 0
                    
                    left = j + l
                    
                else:
                    
                    "加上遇到的单词"
                    valid[sub] = valid.get(sub, 0) + 1
                    
                    
                    if valid[sub] <= need[sub]:
                        cnt += 1
                    else:
                        while valid[sub] > need[sub]:
                            
                            DelStr = s[left:left+l]
                            valid[DelStr] -= 1
                            
                            if valid[DelStr] < need[DelStr]:
                                cnt -= 1
                            
                            left += l
                    
                    if cnt == k:
                        
                        ans.append(left)
                        
                        valid[s[left:left+l]] -= 1
                        
                        cnt -= 1
                        
                        left += l
                            
        return ans