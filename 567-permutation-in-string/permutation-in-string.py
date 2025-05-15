class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s2) < len(s1): return False
        s1hash = {chr(c): 0 for c in range(ord('a'), ord('z')+1)}
        s2hash = s1hash.copy()

        for i in range(len(s1)):
            s1hash[s1[i]] += 1
            s2hash[s2[i]] += 1

        l = 0 
        for r in range(len(s1), len(s2)):
            if s1hash == s2hash:
                return True
            s2hash[s2[l]] -= 1
            l += 1
            s2hash[s2[r]] += 1
        if s1hash == s2hash:
            return True
        else:
            return False