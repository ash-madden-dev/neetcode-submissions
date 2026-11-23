class Solution:
    def canPermutePalindrome(self, s: str) -> bool:
        chars = {}
        count_of_odd_chars = 0
        for char in s:
            if char in chars:
                chars[char] += 1
                if chars[char] % 2 == 1:
                    count_of_odd_chars += 1
                else:
                    count_of_odd_chars -= 1
            else:
                chars[char] = 1
                count_of_odd_chars += 1
        return count_of_odd_chars <= 1
        