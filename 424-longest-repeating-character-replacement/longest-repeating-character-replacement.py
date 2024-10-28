class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        
        
        max_count = 0
        l = 0 
        count = {}
        max_counter = 0

        for r in range(len(s)):
            count[s[r]] = 1 + count.get(s[r], 0)
            max_counter = max(max_counter, count[s[r]])

            if (r - l + 1) - max_counter > k:
                count[s[l]] -= 1
                l += 1
            
            max_count = max(max_count, r - l + 1)
        
        return max_count
