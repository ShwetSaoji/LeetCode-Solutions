class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        hms = {}
        hmt = {}
        for i in range(len(s)):
            if (s[i] in hms and hms[s[i]] != t[i]) or (t[i] in hmt and hmt[t[i]] != s[i]):
                return False
            hms[s[i]] = t[i]
            hmt[t[i]] = s[i]
        return True

        
