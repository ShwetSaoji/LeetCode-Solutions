class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        # if needle not in haystack:
        #     return -1
        
        for i in range(len(haystack) + 1 - len(needle)):
            print(haystack[i:len(needle)])
            if haystack[i:i+len(needle)] == needle:
                return i
        
        return -1