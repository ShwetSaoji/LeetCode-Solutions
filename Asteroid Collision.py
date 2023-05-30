class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        ans = []
        ans.append(asteroids[0])

        for i in range(1, len(asteroids)):
            print(ans)
            while ans[-1] > 0 and asteroids[i] < 0:
                if abs(ans[-1]) < abs(asteroids[i]):
                    ans.pop()
                    #ans.append(asteroids[i])
                elif abs(ans[-1]) == abs(asteroids[i]):
                    ans.pop()
                break
            else:
                ans.append(asteroids[i])
        
        return ans
