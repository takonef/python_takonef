class Solution:
    def isValid(self, s: str) -> bool:
        br = {')': '(', '}': '{', ']': '['}
        stack = []
        
        for ch in s:
            if ch in br:
                if len(stack) == 0 or stack.pop() != br[ch]:
                    return False
            else:
                stack.append(ch)
        
        return not stack