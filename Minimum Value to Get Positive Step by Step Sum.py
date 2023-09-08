class Solution:
    def minStartValue(self, nums: List[int]) -> int:
        temp = 1 - nums[0]
        if temp < 1:
            temp = 1
        
        i = 1
        val = temp + nums[0]

        while i <= len(nums):
            if val < 1:
                temp += 1
                i = 1
                val = temp + nums[0]
            else:
                if i >= len(nums):
                    break
                val = val + nums[i]
                i += 1
        
        return temp
