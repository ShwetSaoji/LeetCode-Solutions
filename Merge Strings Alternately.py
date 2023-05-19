class Solution:
    def mergeAlternately(self, x: str, y: str) -> str:
        res = ""
        mn = min(len(x), len(y))
        for i in range(mn):
            res += x[i]
            res += y[i]
        if len(x) > len(y):
            res += x[mn:]
        else:
            res += y[mn:]
        return res
