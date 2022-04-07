class Solution:
    def duplicateZeros(self, arr: List[int]) -> None:
        """
        Do not return anything, modify arr in-place instead.

        copy from https://leetcode.com/problems/duplicate-zeros/discuss/312727/C%2B%2BJava-Two-Pointers-Space-O(1) lee215
        
        1. 计算一共有几个0。
        2. 假设我们有一个list长度等于 n + zeros， 然后我们设置两个pointer i = n -1, j = n + zeros - 1.
        3. 每当i对应的值等于0， 我们就左移 j 两次， 非0 则左移 j 一次。（j永远在i的右边， j >= i）
        """
        
        num_zero = arr.count(0)
        
        if not num_zero:
            return
        
        n = len(arr)
        
        j =  n + num_zero - 1
        
        for i in range(n-1, -1, -1):
            
            if not arr[i]:
                
                if j <= n - 1:
                    arr[j] = 0
                    
                j -= 1
                
                if j <= n - 1:
                    arr[j] = 0
                    
            else:
                
                if j <= n - 1:
                    arr[j] = arr[i]
                    
            j -= 1
        
        return 