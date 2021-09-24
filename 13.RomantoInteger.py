class Solution:
    def romanToInt(self, s: str) -> int:
        "from left to right"
        digits = {"M":1000, "CM": 900, "D": 500, "CD": 400, "C": 100, 
            "XC":90, "L": 50, "XL": 40, "X": 10, "IX": 9, 
            "V": 5, "IV": 4, "I": 1}
        cur = 0
        result = 0
        while cur < len(s):
            if cur + 1 < len(s) and digits[s[cur]] < digits[s[cur+1]]:
                result += digits[s[cur+1]] - digits[s[cur]]
                cur += 2
            else:
                result += digits[s[cur]]
                cur += 1
        return result

class Solution:
    def romanToInt(self, s: str) -> int:
        "from right to left"
        digits = {"M":1000, "CM": 900, "D": 500, "CD": 400, "C": 100, 
            "XC":90, "L": 50, "XL": 40, "X": 10, "IX": 9, 
            "V": 5, "IV": 4, "I": 1}
        result = 0
        for i in range(len(s) - 1, -1, -1):
            if i + 1 < len(s) and  digits[s[i]] < digits[s[i+1]]:
                result -= digits[s[i]]
            else:
                result += digits[s[i]]
        return result