class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prefix = 1
        pre_arr = [1] * len(nums)

        for i in range(1, len(nums)):
            prefix = prefix * nums[i-1]
            pre_arr[i] = prefix
        
        postfix = 1
        post_arr = [1] * len(nums)
        res = []
        for i in range(len(nums)-2,-1,-1):
            postfix = postfix * nums[i+1]
            post_arr[i] = postfix

        for i in range(len(nums)):
            res.append(pre_arr[i] * post_arr[i])
        
        return res