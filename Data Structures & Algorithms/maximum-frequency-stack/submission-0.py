class FreqStack:

    def __init__(self):
        self.s = []
        self.d = {}

    def push(self, val: int) -> None:
        self.s.append(val)
        self.d[val] = self.d.get(val, 0) + 1

    def pop(self) -> int:
        mf = max(self.d.values())

        for i in range(len(self.s) - 1, -1, -1):
            if self.d[self.s[i]] == mf:
                ans = self.s.pop(i)
                self.d[ans] -= 1
                return ans