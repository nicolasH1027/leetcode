class TrieNode:
    def __init__(self):
        self.child = collections.defaultdict(TrieNode)
        self.freq = collections.defaultdict(int)

class AutocompleteSystem:

    def __init__(self, sentences: List[str], times: List[int]):
        self.root = TrieNode()
        self.search = ''
        self.cur = self.root
        for item, cnt in zip(sentences, times):
            self.insert(item, cnt)
    def input(self, c: str) -> List[str]:
        if c == '#':
            self.insert(self.search, 1)
            self.cur = self.root
            self.search = ''
            return []
        else:
            self.search += c
            self.cur = self.cur.child[c]
            heap, ans = [], []
            for key, val in self.cur.freq.items():
                heapq.heappush(heap, (-val, key))
            for _ in range(min(3, len(heap))):
                _, res = heapq.heappop(heap)
                ans.append(res)
            return ans
            
            
    def insert(self, sentence, freq):
        node = self.root
        for letter in sentence:
            node = node.child[letter]
            node.freq[sentence] += freq


# Your AutocompleteSystem object will be instantiated and called as such:
# obj = AutocompleteSystem(sentences, times)
# param_1 = obj.input(c)