class Solution:
    def isValid(self, s: str) -> bool:
        VALID_OPENING_BRACKETS = {"{", "[", "("}
        VALID_CLOSING_BRACKETS = {"}", "]", ")"}
        opening_brackets = []
        closing_brackets = []
        expected_closing_brackets = []

        for bracket in s:
            if bracket in VALID_OPENING_BRACKETS:
                opening_brackets.append(bracket)
                match bracket:
                    case "{":
                        expected_closing_brackets.append("}")
                    case "[":
                        expected_closing_brackets.append("]")
                    case "(":
                        expected_closing_brackets.append(")")
                    case _:
                        return False
            elif bracket in VALID_CLOSING_BRACKETS and expected_closing_brackets:
                if bracket != expected_closing_brackets.pop():
                    return False        
            else:
                return False
        
        return len(expected_closing_brackets) == 0

        
                        

        