class Solution:
    def getSum(self, a: int, b: int) -> int:
        mask = 0xFFFFFFFF
        
        while b != 0:
            a, b = (a ^ b) & mask, ((a & b) << 1) & mask
        
        max_int = 0x7FFFFFFF
        return a if a < max_int else ~(a ^ mask)
    

"""

细节证明还没有搞懂，但是大致意思如下

解释参考了如下内容
https://www.ruanyifeng.com/blog/2009/08/twos_complement.html
https://stackoverflow.com/questions/12946116/twos-complement-binary-in-python
https://leetcode.com/problems/sum-of-two-integers/discuss/776952/Python-BEST-LeetCode-371-Explanation-for-Python


2 的补码

它是一种数值的转换方法，要分二步完成：

第一步，每一个二进制位都取相反值，0变成1，1变成0。比如，00001000的相反值就是11110111。

第二步，将上一步得到的值加1。11110111就变成11111000。

所以，00001000的2的补码就是11111000。也就是说，-8在计算机（8位机）中就是用11111000表示。

计算机内部采用2的补码（Two's Complement）表示负数。

因为python采用的int没有精度限制，所以采用了不同的表示方法，所以我们得认为地将数字转换成2的补码的形式

假设我们需要转换的数字为 x，那么x的2的补码形式就可以表示为

x & 0xFFFFFFFF

所以，

while b != 0:
    a, b = a ^ b, (a & b) << 1

现在变成

while b != 0:
    a, b = (a ^ b) & mask, ((a & b) << 1) & mask

把一个数转换成其2的补码形式，（假设为32 bit）那么只需要把这个数 x & 0xFFFFFFFF，就可以了。

即人工将所有数字转换为2的补码。  为什么以2的补码的形式运算，最后结果一样？（这个问题请自行翻阅 计算机原理 等书籍）

最后我们得到的结果  a， 现在也是以2的补码的形式存在的，且限定了32位bit

如果 a 小于 0x7FFFFFFF，（0x7FFFFFFF 表示31位bit的数字，最高位表示符号）

那么直接返回 a， 正数

如果大于，说明是负数，需要转换为 python 框架下的负数形式

举例说明，

8，  2的补码， 00001000
-8， 2的补码， 11111000

现在我们有了-8的补码，那么要想得到8的补码，应该怎么做

把-8每一位反转，变成 00000111, 然后加1 得到  00001000

所以

a ^ 0xFFFFFFFF + 1 == 我们想要的数的正数

回忆

~x = -x - 1

结合上面的，可以得到

~(a^0xFFFFFFFF) 就是我们要的数
"""