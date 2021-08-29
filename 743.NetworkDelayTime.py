import collections


class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        
        import heapq
        ADlist = self.convert(times)
        heap = []
        heapq.heappush(heap, (0, k - 1))
        parent = list(range(n))
        seen = set()
        distance = [float(inf)]*n
        distance[k - 1] = 0
        
        while heap:
            w, node = heapq.heappop(heap)
            if node in seen: continue
            seen.add(node)
            for weight, neighbor in ADlist[node]:
                if neighbor not in seen:
                    if w + weight < distance[neighbor]:
                        distance[neighbor] = w + weight
                        parent[neighbor] = node
                        heapq.heappush(heap, (w + weight, neighbor))
        res = max(distance)         
        return res if res != float(inf) else -1
    
    def convert(self, edges):
        ADlist = collections.defaultdict(list)
        for edge in edges:
            ADlist[edge[0] - 1].append((edge[2], edge[1] - 1))
        return ADlist