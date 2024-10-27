class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l = 0
        arr = []
        max_substring = 0

        for r in range(len(s)):
            while s[r] in arr:
                arr.remove(s[l])
                l += 1
            arr.append(s[r])
            max_substring = max(max_substring, r - l + 1)
        return max_substring