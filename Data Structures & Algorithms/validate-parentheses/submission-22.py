class Solution:
    def isValid(self, s: str) -> bool:
        BRACKETS = {"{": "}", "[": "]", "(": ")"}
        if len(s) % 2 != 0 or s[0] in BRACKETS.values():
            return False
        else: 
            expected_bracket = []
            for bracket in s:
                if bracket in BRACKETS: 
                    expected_bracket.append(BRACKETS[bracket])
                elif expected_bracket and bracket != expected_bracket.pop():
                    return False
            return not expected_bracket

        
                        

        