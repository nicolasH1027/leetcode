class Solution:
    def rearrangeString(self, s: str, k: int) -> str:
        
        heap, cnt = [], collections.Counter(s)
        
        maxf = max(cnt.values())
        
        if (maxf - 1) * k + cnt.values().count(maxf) > len(s):
            return ""
        
        for key, count in cnt.items():
            heapq.heappush(heap, (-count, key))

        ans, queue = [], collections.deque()
        
        while heap:
            
            cur, key = heapq.heappop(heap)
            cur += 1
            ans.append(key)
            queue.append((cur, key))

            if len(queue) >= k:
                cur, key = queue.popleft()
                if cur:
                    heapq.heappush(heap, (cur, key))

        return ''.join(ans) if len(ans) == len(s) else ''