class Solution:
    def maxVowels(self, s: str, k: int) -> int:

        m = 0
        count = 0
        
        for i in range(len(s)):

            if i >= k:
                if s[i-k] in "aeiou":
                    count -= 1
            if s[i] in "aeiou":
                count += 1
            
            m = max(m,count)
        
        return m
