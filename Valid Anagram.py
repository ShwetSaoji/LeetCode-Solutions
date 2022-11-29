class Solution:
    def isAnagram(self, s: str, t: str) -> bool:

        if len(s) != len(t): 
            return False

        a=sorted(s)
        b=sorted(t)

        for i in range(len(a)):
            if a[i] != b[i]:
                return False

        return True 
