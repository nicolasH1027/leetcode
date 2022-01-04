class Solution:
    def bitwiseComplement(self, n: int) -> int:
        "bit by bit"
        if n == 0:
            return 1
        
        cur, op = n, 1
        
        while cur:
            n ^= op
            cur =  cur >> 1
            op = op << 1
            
        return n


class Solution:
    def bitwiseComplement(self, n: int) -> int:
        
        return (1 << n.bit_length()) -1 - n if n else 1