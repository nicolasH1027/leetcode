
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
"""




