class Solution:
    def reverseVowels(self, s: str) -> str:
        #v = ['a','i','e','o','u']
        s = list(s)
        res = []
        for i in s:
            if i in "aeiouAEIOU":
                res.append(i)
        
        res.reverse()

        pos = 0
        for i in range(len(s)):
            if s[i] in "aeiouAEIOU":
                s[i] = res[pos]
                pos += 1

        return "".join(s)
