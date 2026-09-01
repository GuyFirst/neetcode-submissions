class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = s.lower()
        left = 0
        right = len(s) - 1
        while left < right:
            if not s[left].islower() and not s[left].isdigit():
                left += 1
                continue
            elif not s[right].islower() and not s[right].isdigit():
                right -= 1
                continue
            elif s[left] != s[right]:
                return False
            left += 1
            right -= 1
        return True
        
        