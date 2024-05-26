class Solution:
    def reverseVowels(self, s: str) -> str:
        l , r = 0 , len(s) -1
        s = list(s)
        while l < r:
            if s[l] in "aeiouAEIOU" and s[r] in "aeiouAEIOU":
                s[l], s[r] = s[r], s[l]
                l+=1
                r-=1
            else:
                if s[l] not in "aeiouAEIOU":
                    l += 1
                if s[r] not in "aeiouAEIOU":
                    r -= 1
        
        return ''.join(s)
            