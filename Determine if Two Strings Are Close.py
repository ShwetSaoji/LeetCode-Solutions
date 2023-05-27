class Solution:
    def closeStrings(self, word1: str, word2: str) -> bool:
        dc1 = {}
        dc2 = {}
        if set(word1) != set(word2):
            return False
        for i in word1:
            if i not in dc1:
                dc1[i] = 1
            else:
                dc1[i] += 1
        for i in word2:
            if i not in dc2:
                dc2[i] = 1
            else:
                dc2[i] += 1
        
        if sorted(dc1.values()) != sorted(dc2.values()):
            return False
        
        return True
