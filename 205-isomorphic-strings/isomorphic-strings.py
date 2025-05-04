class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        hm_s = {}
        hm_t = {}

        for i in range(len(s)):
            if (s[i] in hm_s and hm_s[s[i]] != t[i])  or (t[i] in hm_t and hm_t[t[i]] != s[i]):
                return False
            hm_s[s[i]] = t[i]
            hm_t[t[i]] = s[i]

        return True