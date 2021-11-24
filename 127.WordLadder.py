import collections


class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        """
        BFS,
        
        """
        candidate = set(wordList)
        if endWord not in candidate:
            return 0
        
        if endWord not in wordList or not endWord or not beginWord or not wordList:
            return 0

        # Since all words are of same length.
        L = len(beginWord)

        # Dictionary to hold combination of words that can be formed,
        # from any given word. By changing one letter at a time.
        all_combo_dict = defaultdict(list)
        for word in wordList:
            for i in range(L):
                # Key is the generic word
                # Value is a list of words which have the same intermediate generic word.
                all_combo_dict[word[:i] + "*" + word[i+1:]].append(word)


        # Queue for BFS
        queue = collections.deque([(beginWord, 1)])
        # Visited to make sure we don't repeat processing same word.
        visited = {beginWord: True}
        while queue:
            current_word, level = queue.popleft()
            for i in range(L):
                # Intermediate words for current word
                intermediate_word = current_word[:i] + "*" + current_word[i+1:]

                # Next states are all the words which share the same intermediate state.
                for word in all_combo_dict[intermediate_word]:
                    # If at any point if we find what we are looking for
                    # i.e. the end word - we can return with the answer.
                    if word == endWord:
                        return level + 1
                    # Otherwise, add it to the BFS Queue. Also mark it visited
                    if word not in visited:
                        visited[word] = True
                        queue.append((word, level + 1))
                all_combo_dict[intermediate_word] = []
        return 0
    
    

class Solution(object):
    def ladderLength(self, beginWord, endWord, wordList):
        """
        :type beginWord: str
        :type endWord: str
        :type wordList: List[str]
        :rtype: int
        """
        
        def bfs(queue, visted, other_visited):
            word, level = queue.popleft()
            for i in range(L):
                intermediate = word[:i] + '*' + word[i+1:]
                for target in dic[intermediate]:
                    if target in other_visited:
                        return level + other_visited[target]
                    if target in visted: continue
                    visted[target] = level + 1
                    queue.append((target, level + 1))
            return None
        
        L = len(beginWord)
        dic = collections.defaultdict(list)
        for word in wordList:
            for i in range(L):
                dic[word[:i] + '*' + word[i+1:]].append(word)
                
        begin_visted = {beginWord:1}
        end_visited = {endWord:1}
        
        begin_queue = collections.deque([(beginWord, 1)])
        end_queue = collections.deque([(endWord, 1)])
        
        while begin_queue and end_queue:
            
            ans = bfs(begin_queue, begin_visted, end_visited)
            if ans:
                return ans
            
            ans = bfs(end_queue, end_visited, begin_visted)
            if ans:
                return ans
        
        return 0
            