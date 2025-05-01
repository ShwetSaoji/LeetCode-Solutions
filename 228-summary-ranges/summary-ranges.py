class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        ans = []
        if len(nums) == 0:
            return []
        else:
            temp = [nums[0]]

        for i in range(1, len(nums)):
            if nums[i] - nums[i-1] == 1:
                temp.append(nums[i])
            else:
                ans.append(temp)
                temp = [nums[i]]
        ans.append(temp)
        ansstr = []
        print(ans)
        for i in ans:
            if len(i) > 1:
                ansstr.append(str(min(i)) + "->" + str(max(i)))
            else:
                ansstr.append(str(i[0]))
        
        return ansstr