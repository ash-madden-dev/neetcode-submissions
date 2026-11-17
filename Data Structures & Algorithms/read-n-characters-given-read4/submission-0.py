class Solution:
    def __init__(self):
        pass

    def read(self, buf: List[str], n: int) -> int:
        total = 0
        tmp = [''] * 4
        while total < n:
            count = read4(tmp)
            if count == 0:
                break
            take = min(count, n - total)
            buf[total:total + take] = tmp[:take]
            total += take
            if count < 4:
                break
        return total