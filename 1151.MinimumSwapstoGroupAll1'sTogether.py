class Solution:
    def minSwaps(self, data: List[int]) -> int:
        
        n, one = len(data), sum(data)
        MoveSum = sum(data[:one])
        ans = MoveSum
        
        for i in range(one, n):
            MoveSum += data[i]
            MoveSum -= data[i-one]
            ans = max(ans, MoveSum)
        return one - ans
            
            