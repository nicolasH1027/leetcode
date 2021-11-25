class Solution:
    def findLadders(self, beginWord: str, endWord: str, wordList: List[str]) -> List[List[str]]:

        candidate = set(wordList)
        if endWord not in candidate:
            return []
        
        L, seen, dic = len(beginWord), set([beginWord]), collections.defaultdict(list)
        
        for word in wordList:
            for i in range(L):
                intermediate = word[:i] + '*' + word[i+1:]
                dic[intermediate].append(word)
                
        queue = collections.deque([(beginWord, [beginWord])])
        ans = []
        
        while queue and not ans:
            
            cur_seen = set()
            
            for _ in range(len(queue)):
                
                word, path = queue.popleft()
                
                for i in range(L):
                    for target in dic[word[:i] + '*' + word[i+1:]]:
                        if target == endWord:
                            ans.append(path + [target])
                        if target in seen: continue
                        
                        cur_seen.add(target)
                        queue.append((target, path + [target]))
                        
            seen = seen.union(cur_seen)
            
        return ans
    

class Solution:
    def findLadders(self, beginWord: str, endWord: str, wordList: List[str]) -> List[List[str]]:

        if not endWord or not beginWord or not wordList or endWord not in wordList \
            or beginWord == endWord:
            return []

        L = len(beginWord)

        # Dictionary to hold combination of words that can be formed,
        # from any given word. By changing one letter at a time.
        all_combo_dict = collections.defaultdict(list)
        for word in wordList:
            for i in range(L):
                all_combo_dict[word[:i] + "*" + word[i+1:]].append(word)

        # Build graph, BFS
        # ans = []
        queue = collections.deque()
        queue.append(beginWord)
        parents = collections.defaultdict(set)
        visited = set([beginWord])
        found = False 
        depth = 0
        while queue and not found:
            depth += 1 
            length = len(queue)
            localVisited = set()
            for _ in range(length):
                word = queue.popleft()
                for i in range(L):
                    for nextWord in all_combo_dict[word[:i] + "*" + word[i+1:]]:
                        if nextWord not in visited:
                            parents[nextWord].add(word)
                            if nextWord == endWord:    
                                found = True
                            localVisited.add(nextWord)
                            queue.append(nextWord)
            visited = visited.union(localVisited)

        ans = []
        def dfs(node, path, d):
            if d == 0:
                if path[-1] == beginWord:
                    ans.append(path[::-1])
                return 
            for parent in parents[node]:
                path.append(parent)
                dfs(parent, path, d-1)
                path.pop()
        dfs(endWord, [endWord], depth)
        return ans