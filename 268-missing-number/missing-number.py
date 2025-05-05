class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        nums = sorted(nums)
        curr = 0
        n = len(nums)
        while n > 0:
            if curr not in nums:
                return curr
            else:
                curr += 1
                n -= 1
        return len(nums)
        
