import collections
class Solution:

    def alienOrder(self, words: List[str]) -> str:
        
        indegree = collections.defaultdict(int)
        outdege = collections.defaultdict(set)
        
        for word in words:
            for letter in word:
                indegree[letter] = 0
        
        for first, second in zip(words, words[1:]):
            for i, j in zip(first, second):
                if i != j:
                    if j not in outdege[i]:
                        indegree[j] += 1
                        outdege[i].add(j)
                    break
            else:
                if len(second) < len(first):
                    return ""
        
        stack = []
        
        for key in indegree.keys():
            if indegree[key] == 0:
                stack.append(key)
        result = []
        while stack:
            cur = stack.pop()
            result.append(cur)
            
            for target in outdege[cur]:
                indegree[target] -= 1
                if indegree[target] == 0:
                    stack.append(target)
        
        return "".join(result) if len(result) == len(indegree) else ""
    