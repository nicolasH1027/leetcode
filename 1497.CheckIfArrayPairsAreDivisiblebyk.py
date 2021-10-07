class Solution:
    def canArrange(self, arr: List[int], k: int) -> bool:
        "O(N) time, O(N) space"
        rem = collections.defaultdict(int)
        count = 0
        for val in arr:
            """
            (X + Y) % k == 0  ==> x % k == -Y % k 
            """
            if rem[-val % k]:
                count += 2
                rem[-val % k] -= 1
            else:
                rem[val % k] += 1
        
        return count == len(arr)