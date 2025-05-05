class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        s = list(s)
        for i in t:
            if i in s:
                s.remove(i)
            else:
                return i 
            