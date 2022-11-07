class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        dictnums = {}
        
        for i, n in enumerate(nums):
            diff = target - n
            if diff in dictnums:
                return [dictnums[diff] , i]
            dictnums[n] = i
