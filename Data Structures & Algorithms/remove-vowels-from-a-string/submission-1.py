class Solution:
    def removeVowels(self, s: str) -> str:
        new_s = ""
        for char in s:
            if char not in "aeiou":
                new_s += char
        return new_s
