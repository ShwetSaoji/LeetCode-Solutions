class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        if needle not in haystack:
            return -1
        
        for i in range(len(haystack) - len(needle) + 1):
            print(haystack[i:len(needle)+i])
            if haystack[i:len(needle)+i] == needle:
                return i