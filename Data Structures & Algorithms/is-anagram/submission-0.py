class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        letters = [0] * 26
        
        for char in s:
            letters[ord(char) - ord('a')] += 1
            
        for char in t:
            letters[ord(char) - ord('a')] -= 1
            
        for num in letters:
            if num != 0:
                return False
                
        return True