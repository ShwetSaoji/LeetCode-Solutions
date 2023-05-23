class Solution:
    def maxOperations(self, nums: List[int], k: int) -> int:

        count = 0 
        nums.sort()

        l , r = 0, len(nums)-1

        while l < r:
            summ = nums[l] + nums[r]

            if summ == k:
                count += 1
                l += 1
                r -= 1
            elif summ > k:
                r -=1
            else:
                l += 1
        
        
        return count
