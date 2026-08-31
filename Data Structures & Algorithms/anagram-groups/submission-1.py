class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        seen = defaultdict(list)
        
        for s in strs:
            letters = [0] * 26  # האתחול עבר לתוך הלולאה
            for char in s:
                letters[ord(char) - ord('a')] += 1  # סוגריים עגולים ב-ord
            
            # שימוש ב-tuple כמפתח והוספה עם append
            seen[tuple(letters)].append(s)
            
        return list(seen.values())