class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        replace = 0 
        for i in range(len(nums)):
            if nums[i] == 0:
                continue
            else:
                nums[replace], nums[i]= nums[i], nums[replace]
                replace += 1
    