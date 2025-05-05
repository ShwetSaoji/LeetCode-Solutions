class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        output = []
        if len(nums) == 0:
            return []
        lower = nums[0]
        for i in range(1, len(nums)):
            if nums[i] - nums[i-1] == 1:
                continue
            else:
                if lower == nums[i-1]:
                    output.append(str(lower))
                else:
                    output.append(str(lower) + '->' +  str(nums[i-1]))
                lower = nums[i]

        if lower == nums[-1]:
            output.append(str(lower))
        else:
            output.append(str(lower) + '->' +  str(nums[-1]))
        
        return output
        
