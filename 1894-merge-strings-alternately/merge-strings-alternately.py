class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        mn = min(len(word1), len(word2))
        res = ""
        for i in range(mn):
            res += word1[i]
            res += word2[i]
        
        if len(word1) > mn:
            res += word1[mn:]
        if len(word2) > mn:
            res += word2[mn:]

        return res

