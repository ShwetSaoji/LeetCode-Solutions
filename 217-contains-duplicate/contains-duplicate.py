class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        if len(nums) == len(set(nums)):
            return False
        else:
            for i in range(len(nums)-1):
                if nums[i] in nums[i+1:]:
                    return True