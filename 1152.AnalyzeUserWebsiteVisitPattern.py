class Solution:
    def mostVisitedPattern(self, username: List[str], timestamp: List[int], website: List[str]) -> List[str]:
        
        dic = collections.defaultdict(list)
        
        for user, time, web in sorted(zip(username, timestamp, website), key = lambda x: (x[1], x[2])):
            dic[user].append(web)
            
        pattern = collections.Counter()
        
        for _, web in dic.items():
            pattern.update(set(itertools.combinations(web, 3)))
 
        return max(sorted(pattern), key = pattern.get)