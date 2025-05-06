class Solution:
    def fizzBuzz(self, n: int) -> List[str]:
        i = 1
        ans = []
        while n > 0:
            if i%3==0 and i%5==0:
                ans.append("FizzBuzz")
            elif i%3==0:
                ans.append("Fizz")
            elif i%5==0:
                ans.append("Buzz")
            else:
                ans.append(str(i))
            i += 1
            n -= 1
        return ans