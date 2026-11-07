class Solution:
    def calPoints(self, operations: List[str]) -> int:
        r = [] # record
        s = 0 # sum
        for op in operations:
            if op == "+":
                t = r[-1] + r[-2]
                r.append(t)
                s += t
            elif op == "D":
                d = r[-1] * 2
                r.append(d)
                s += d
            elif op == "C":
                s -= r.pop()
            else:
                n = int(op)
                r.append(n)
                s += n
        return s
        