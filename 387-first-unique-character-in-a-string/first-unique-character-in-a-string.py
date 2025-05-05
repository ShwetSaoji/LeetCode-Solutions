class Solution:
    def firstUniqChar(self, s: str) -> int:
        seen = set()
        for i in range(len(s)):
            if  s[i] in s[i+1:len(s)]:
                seen.add(s[i])
            elif s[i] not in s[i+1:len(s)] and s[i] not in seen:
                return i 

        
        return -1


        