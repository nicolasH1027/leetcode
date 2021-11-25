class Solution:
    def longestWord(self, words: List[str]) -> str:
        
        Trie = {}
        END = 'end'
        
        for word in words:
            node = Trie
            for letter in word:
                node = node.setdefault(letter, {})
            node[END] = END
            node['word'] = word
        
        queue = collections.deque([Trie[key] for key in Trie.keys()])
        res = ''
        
        while queue:
            cur = queue.popleft()
            
            if END in cur:
                if len(cur['word']) > len(res) or cur['word'] < res:
                    res = cur['word'] 
                for key in cur.keys():
                    if key != END and key != 'word':
                        queue.append(cur[key])
        return res
