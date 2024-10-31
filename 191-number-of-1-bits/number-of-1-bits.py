class Solution:
    def hammingWeight(self, n: int) -> int:
        arr = []
        while n > 1:
            arr.append(n%2)
            n = n//2
        ans = 1
        arr = arr[::-1]
        for i in arr:
            if i == 1:
                ans += 1
        
        return ans