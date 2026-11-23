class Solution:
    def canPermutePalindrome(self, s: str) -> bool:
        one_odd_char_found = False

        chars = {}
        for char in s:
            if char in chars:
                chars[char] += 1
            else:
                chars[char] = 1
        
        if len(chars) == 1:
            return True
        
        for val in chars.values():
            if val % 2 == 1 and not one_odd_char_found:
                one_odd_char_found  = True
            elif val % 2 == 1 and one_odd_char_found:
                return False
            elif val % 2 != 0:
                return False
        return True