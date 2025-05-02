class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        n = len(nums)
        i = 0
        while n > 0:
            if i in nums:
                n-=1
                i += 1
            else:
                return i
        return i