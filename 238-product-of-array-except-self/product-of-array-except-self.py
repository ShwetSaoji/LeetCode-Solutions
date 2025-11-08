class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        pre = [1] * len(nums)

        for i in range(1, len(nums)):
            pre[i] = pre[i-1] * nums[i-1]
        
        post = [1] * len(nums)

        for i in range(len(nums) - 2, -1, -1):
            post[i] = post[i + 1] * nums[i + 1]
        
        res = [1] * len(nums)
        for i in range(len(nums)):
            res[i] = pre[i] * post[i]
        
        return res