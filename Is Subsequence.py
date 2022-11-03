class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        
        sl,tl = 0, 0 
        
        while sl < len(s) and tl < len(t):
            if s[sl] == t[tl]:
                sl += 1
                tl += 1
            else:
                tl += 1
        
        if sl == len(s):
            return True
        else:
            return False
