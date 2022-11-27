class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        ins = 1
        for r in range(1, len(nums)):
            if nums[r] != nums[r-1]:
                nums[ins] = nums[r]
                ins += 1
        
        return ins
