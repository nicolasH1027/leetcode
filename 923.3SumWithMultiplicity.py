class Solution:
    def threeSumMulti(self, arr: List[int], target: int) -> int:
        """
        Navie way, but TLE
        """
        n = len(arr)
        self.result = 0
        MOD = 10**9 + 7
        def backtrack(arr, target, start, k):
            
            if target == 0 and k == 0:
                self.result += 1
                return 
            if k <= 0:
                return 
            
            for i in range(start, n):
                backtrack(arr, target - arr[i], i+1, k - 1)

        backtrack(arr, target, 0, 3)
        return self.result % MOD
    

class Solution:
    def threeSumMulti(self, arr: List[int], target: int) -> int:
        " Counting frequency "
        
        MOD = 10**9 + 7
        count = collections.Counter(arr)
        keys = sorted(count)        # we only need to iterate the distinct value
        n = len(keys)
        res = 0
        
        for i in range(n):
            tmp = target - keys[i]
            j, k = i,  n - 1
            while j <= k:
                y, z = keys[j], keys[k]
                if y + z < tmp:
                    j += 1
                elif y + z > tmp:
                    k -= 1
                else:           # counting the how many different combinations
                    if i == j == k:
                        res += count[keys[i]] * (count[keys[i]] - 1) * (count[keys[i]] - 2) // 6
                    elif i == j != k:
                        res += count[keys[i]] * (count[keys[i]] - 1) * count[keys[k]] // 2
                    elif i != j == k:
                        res += count[keys[j]] * (count[keys[j]] - 1) * count[keys[i]] // 2
                    else:
                        res += count[keys[i]] * count [keys[j]] * count[keys[k]]
                    j += 1
                    k -= 1
        return res % MOD


class Solution(object):
    def threeSumMulti(self, A, target):
        MOD = 10**9 + 7
        ans = 0
        A.sort()

        for i, x in enumerate(A):
            # look at the difference between this and the above
            # cause we iterate from the original array, so, j = i + 1
            T = target - A[i]
            j, k = i+1, len(A) - 1

            while j < k:

                if A[j] + A[k] < T:
                    j += 1
                elif A[j] + A[k] > T:
                    k -= 1

                elif A[j] != A[k]:                              # we need to remove the repeated cases
                                                                # count the repeat times of pairs
                    left = right = 1
                    while j + 1 < k and A[j] == A[j+1]:
                        left += 1
                        j += 1
                    while k - 1 > j and A[k] == A[k-1]:
                        right += 1
                        k -= 1

                    # We contributed left * right many pairs.
                    ans += left * right
                    ans %= MOD
                    j += 1
                    k -= 1

                else:
                    # M = k - j + 1
                    # We contributed M * (M-1) / 2 pairs.
                    ans += (k-j+1) * (k-j) / 2
                    ans %= MOD
                    break

        return ans