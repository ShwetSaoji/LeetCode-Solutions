class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:

        pre = 1
        post = 1
        prea = len(nums) * [1]
        posta = len(nums) * [1]

        for i in range(len(nums)):
            prea[i] = pre
            pre *= nums[i]
        
        for i in range(len(nums)-1, -1, -1):
            posta[i] = post
            post *= nums[i]
            posta[i] *= prea[i]
        
        return posta
