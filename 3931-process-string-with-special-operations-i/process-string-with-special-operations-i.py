class Solution:
    def processStr(self, s: str) -> str:
        res = ""

        for char in s:
            if char == '*':
                if len(res) > 0:
                    slist = list(res)
                    slist.pop()
                    res = ''.join(slist)
            elif char =="#":
                res = res + res
            elif char == "%":
                slist = list(res)
                slist = slist[::-1]
                res = ''.join(slist)
            else:
                res += char
        return res