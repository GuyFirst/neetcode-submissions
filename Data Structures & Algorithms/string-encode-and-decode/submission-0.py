class Solution:

    def encode(self, strs: List[str]) -> str:
        main_shift = len(strs)
        res_list = [f"{main_shift}#"]
        
        for s in strs:
            res_list.append(f"{len(s)}#")
            for char in s:
                res_list.append(chr(ord(char) + len(s)))
                
        joined_str = "".join(res_list)
        
        final_shifted_list = []
        for char in joined_str:
            final_shifted_list.append(chr(ord(char) + main_shift))
            
        return "".join(final_shifted_list)

    def decode(self, s: str) -> List[str]:
        if not s: 
            return []
        
        main_shift = 0
        start_idx = 0
        
        for i in range(len(s)):
            candidate_shift = ord(s[i]) - ord('#')
            
            if candidate_shift >= 0:
                prefix = "".join(chr(ord(c) - candidate_shift) for c in s[:i])
                
                if prefix == str(candidate_shift):
                    main_shift = candidate_shift
                    start_idx = i + 1
                    break
        
        base_chars = []
        for char in s[start_idx:]:
            base_chars.append(chr(ord(char) - main_shift))
        base_str = "".join(base_chars)
        
        res = []
        i = 0
        while i < len(base_str):
            delim_idx = base_str.find('#', i)
            if delim_idx == -1:
                break
            
            word_len = int(base_str[i:delim_idx])
            i = delim_idx + 1
            
            shifted_word = base_str[i : i + word_len]
            original_word = "".join(chr(ord(c) - word_len) for c in shifted_word)
            res.append(original_word)
            
            i += word_len
            
        return res
        
