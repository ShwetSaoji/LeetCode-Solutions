class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        # cnt = 1
        # ans = []

        # for i in range(len(temperatures)):
        #     for j in range(i+1, len(temperatures)):
        #         if j == len(temperatures)-1 and temperatures[j] <= temperatures[i]:
        #             ans.append(0)
        #             cnt = 1
        #         elif temperatures[j] > temperatures[i]:
        #             ans.append(cnt)
        #             cnt = 1
        #             break
        #         else:
        #             cnt += 1
        
        
        # ans.append(0)
        # return ans

        ans = [0] * len(temperatures)
        stack = []

        for i, t in enumerate(temperatures):
            while stack and t > stack[-1][1]:
                ind, temp = stack.pop()
                ans[ind] = i - ind
            stack.append([i , t])
        return ans


