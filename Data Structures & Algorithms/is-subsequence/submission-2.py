class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        if not s:
            return True
        s_chars = list(s)
        for char in t:
            if s_chars and char == s_chars[0]:
                del s_chars[0]
        return not s_chars
        
