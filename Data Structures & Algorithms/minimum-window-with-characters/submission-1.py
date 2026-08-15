class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if len(s) < len(t):
            return ""

        t1 = {}
        s1 = {}

        for ch in t:
            t1[ch] = t1.get(ch, 0) + 1

        required = len(t1)

        l = 0
        mini = float('inf')
        ans = ""
        f = 0

        for i in range(len(s)):
            s1[s[i]] = s1.get(s[i], 0) + 1

            if s[i] in t1 and s1[s[i]] == t1[s[i]]:
                f += 1

            while f == required:

                if i - l + 1 < mini:
                    mini = i - l + 1
                    ans = s[l:i + 1]

                left = s[l]
                s1[left] -= 1

                if left in t1 and s1[left] < t1[left]:
                    f -= 1

                l += 1

        return ans