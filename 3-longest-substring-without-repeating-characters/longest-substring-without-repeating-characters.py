class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l = 0 
        currSet = set()
        maxSubstring = 0 
        
        for r in range(len(s)):
            while s[r] in currSet:
                
                currSet.remove(s[l])
                l += 1
            currSet.add(s[r])
            maxSubstring = max(r - l + 1, maxSubstring)
        
        return maxSubstring

# class Solution:
#     def lengthOfLongestSubstring(self, s: str) -> int:
#         charSet = set()
#         l = 0
#         res = 0

#         for r in range(len(s)):
#             while s[r] in charSet:
#                 charSet.remove(s[l])
#                 l += 1
#             charSet.add(s[r])
#             res = max(res, r - l + 1)
#         return res