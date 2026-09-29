from collections import Counter

class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        abc = Counter(magazine)
        
        for ch in ransomNote:
            if abc[ch] <= 0:
                return False
            abc[ch] -= 1
            
        return True