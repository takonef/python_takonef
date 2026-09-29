class Solution:
    def romanToInt(self, s: str) -> int:
        roman_map = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
        
        sum = 0
        prev = 0
        
        for ch in reversed(s):
            val = roman_map[ch]
            if val < prev:
                sum -= val
            else:
                sum += val
            prev = val
            
        return sum