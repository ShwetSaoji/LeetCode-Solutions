class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prefix = [1] * len(nums)
        for i in range(1, len(nums)):
            prefix[i] = nums[i-1] * prefix[i-1]
            
        postfix = [1] * len(nums)
        for i in range(len(nums) -2, -1, -1):
            postfix[i] = nums[i+1] * postfix[i+1]
        
        res = [1] * len(nums)
        for i in range(len(nums)):
            res[i] = postfix[i] * prefix[i]

        return res
