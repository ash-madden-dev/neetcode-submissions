class Solution:
    def validWordSquare(self, words: List[str]) -> bool:
        row = []
        col = []
        for i in range(len(words)):
            for j in range(len(words[i])):
                row.append(words[i][j])
            for k in range(len(words)):
                if i < len(words[k]):
                    col.append(words[k][i])
            if row != col:
                return False
            else:
                row = []
                col = []
        return True
            