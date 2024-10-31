class Solution:
    def hammingWeight(self, n: int) -> int:
        ans = 1
        while n > 1:
            if n%2 == 1:
                ans += 1
            n = n//2
        
        
        return ans