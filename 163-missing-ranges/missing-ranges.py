class Solution:
    def findMissingRanges(self, nums: List[int], lower: int, upper: int) -> List[List[int]]:
        output = []

        if len(nums) == 0:
            return [[lower, upper]]
        if nums[0] > lower:
            output.append([lower, nums[0] - 1])
        
        for i in range(len(nums) - 1):
            if nums[i+1] - nums[i] == 1:
                continue
            else:
                output.append([nums[i] + 1, nums[i+1] -1])
        
        if nums[-1] < upper:
            output.append([nums[-1]+1, upper])
        
        return output