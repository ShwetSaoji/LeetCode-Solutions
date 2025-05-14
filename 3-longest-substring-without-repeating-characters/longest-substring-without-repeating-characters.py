class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        charSet = set()
        ans = 0 
        l = 0 
        for i in range(len(s)):
            while s[i] in charSet:
                charSet.remove(s[l])
                l += 1
            charSet.add(s[i])
            ans = max(ans, i - l + 1)
        return ans
