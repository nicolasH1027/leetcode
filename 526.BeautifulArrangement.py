class Solution:
    def countArrangement(self, n: int) -> int:
        def backtrack(track, seen):
            if len(track) == n:
                self.result += 1
                return
            for i in range(1, n + 1):
                if i in seen: continue
                if (len(track)+1) % i == 0 or i % (len(track)+1) == 0:
                    seen.add(i)
                    track.append(i)
                    backtrack(track, seen)
                    track.pop()
                    seen.remove(i)
        seen = set()
        self.result = 0
        backtrack([], seen)
        return self.result