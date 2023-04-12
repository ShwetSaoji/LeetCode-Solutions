class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        
        charSet = set()
        ans = 0 

        l = 0 

        for r in range(len(s)):
            while s[r] in charSet:
                charSet.remove(s[l])
                l +=1
            charSet.add(s[r])
            print(charSet)
            ans = max(ans, r - l + 1)
        return ans
