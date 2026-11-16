class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        letter_found = False
        count = 0
        for char in s[::-1]:
            if char != " " and not letter_found:
                letter_found = True
            if letter_found and char != " ":
                count += 1
            if letter_found and char == " ":
                return count
        return count