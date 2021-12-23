class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:

        freq = collections.Counter(words)
        
        dic = collections.defaultdict(list)
        
        length = 0
        for key, val in freq.items():
            dic[val].append(key)
            length = max(length, val)
            
        arr = [0]*length
        
        for key in dic.keys():
            arr[key-1] = 1
        
        
        ans = []
        
        for i in range(length-1, -1, -1):
            
            if arr[i] == 0:
                continue
            
            if k > 0:
                cnt = len(dic[i + 1])
                dic[i + 1].sort()
                ans.extend(dic[i + 1][:min(k, cnt)])
                k -= cnt
            
            if k <= 0:
                return ans
            

class word:
    
    def __init__(self, word, freq):
        
        self.word = word
        self.freq = freq
    
    def __lt__(self, other):
        if self.freq == other.freq:
            return self.word > other.word
        return self.freq < other.freq
    
    def __eq__(self, other):
        
        return self.freq == other.freq and self.word == other.word
    
class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        
        cnt = collections.Counter(words)
        
        heap = []
        
        print(cnt)
        
        for key, freq in cnt.items():
            
            heapq.heappush(heap, word(key, freq))
            if len(heap) > k:
                heapq.heappop(heap)

        
        ans = []
        
        while heap:
            ans.append(heapq.heappop(heap).word)
        
        return ans[::-1]


            