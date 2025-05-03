class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        replace = 1
        k = 1
        for i in range(1, len(nums)):
            if nums[i] == nums[i-1]:
                continue
            else:
                nums[replace] = nums[i]
                replace += 1
        return replace
