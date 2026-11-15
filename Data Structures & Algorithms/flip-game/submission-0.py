class Solution:
    def generatePossibleNextMoves(self, currentState: str) -> List[str]:
        reachable_positions = []
        for i in range(len(currentState) - 1):
            if currentState[i] == "+" and currentState[i + 1] == "+":
                if i == 0:
                    reachable_positions.append("--" + currentState[2:])
                else:
                    reachable_positions.append(currentState[0:i] + "--" + currentState[i + 2:])
        return reachable_positions

