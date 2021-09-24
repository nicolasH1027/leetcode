class Solution:
    def intToRoman(self, num: int) -> str:
        """
        lets say 1547
        1547 - 1000 = 547
        M
        547 - 500 = 47
        MD
        47-40 = 7
        MDXL
        7 - 5 = 2
        MDXLV
        2 - 1= 1
        MDXLVI
        1 - 1= 0
        MDXLVII
        """
        digits = [(1000, "M"), (900, "CM"), (500, "D"), (400, "CD"), (100, "C"), 
            (90, "XC"), (50, "L"), (40, "XL"), (10, "X"), (9, "IX"), 
            (5, "V"), (4, "IV"), (1, "I")]
        
        res = []
        for value, symbol in digits:
            if num == 0: break
            count, num = divmod(num, value)
            res.append(symbol*count)
        return "".join(res)