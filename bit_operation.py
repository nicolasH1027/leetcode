
"""
a is a number

a ^ a = 0
a ^ 0 = a

a^b^a = a^a^b

remove the last 1 in bit

a & (a - 1)

or

a & (a - 1) == 0 can be used test whether a is the exopnent of 2


binary addition

we use the & and << to get the carry

add(a, b)

while a:

    carry = a & b
    b = a ^ b
    a = carry

return b


~a == -a - 1
首先计算a的补码
1.
正数和0的补码就是其本身
负数的补码为 除符号位，其它按位取反，然后再加一

2.
然后将取得的补码转为反码，既按位取反（包含符号位）

~9

bin(9) == 0 1001

取补码得

01001 （正数补码不变）

取反码得
10110

注意，因为计算机储存的是补码而不是原码，因此
计算机会将 10110 视为补码

（补码再转为原码，正数的补码就是原码。 负数的补码，
符号位不变，其余按位取反，然后加1）

因此

10110 按位取反得（除符号位）
11001
再加1

11010 

为-10

"""




