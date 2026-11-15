class Solution:
    def removeVowels(self, s: str) -> str:
        new_s = ""
        for char in s:
            if char != "a" and char != "e" and char != "i" and char != "o" and char != "u":
                new_s += char
        return new_s
