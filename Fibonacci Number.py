class Solution:
    def fib(self, n: int) -> int:
        
        
        if n == 2 or n == 1:
            return 1
        elif n == 0:
            return 0
        arr = [0 ,1]
        temp = 0
        for i in range(2, n+1):
            temp = arr[i -1] + arr[i -2]
            arr.append(temp)
        
        return arr[-1]
