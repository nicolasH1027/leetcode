class Solution:

    from collections import defaultdict, Counter, deque

    def alienOrder(self, words: List[str]) -> str:
        
        indegree = collections.defaultdict(dict)
        
        for word in words:
            for letter in word:
                indegree[letter] = 0
                
        outdegree = collections.defaultdict(set)
        
        for first, second in zip(words, words[1:]):
            for i, j in zip(first, second):
                if i != j:
                    if j not in outdegree[i]:
                        outdegree[i].add(j)
                        indegree[j] += 1
                    break
            else:
                if len(second) < len(first):
                    return ""
                
        result = []
        queue= deque()
        for key in indegree.keys():
            if indegree[key] == 0:
                queue.append(key)
        
        while queue:
            cur = queue.popleft()
            result.append(cur)
            for tar in outdegree[cur]:
                indegree[tar] -= 1
                if indegree[tar] == 0:
                    queue.append(tar)
            # del outdegree[cur]
        
        return "".join(result) if len(result) == len(indegree) else ""
                    