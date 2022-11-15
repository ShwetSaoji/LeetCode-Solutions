class Solution:
    def climbStairs(self, n: int) -> int:
        
        if n == 1: return 1
        arr = [1, 2]
        
        for i in range(2, n):
            arr.append(arr[i -1] + arr[i -2])
        
        return arr[-1]
