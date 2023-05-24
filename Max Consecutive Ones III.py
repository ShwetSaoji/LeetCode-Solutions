class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:

        l , m = 0, 0

        for r, n in enumerate(nums):
            if n == 0:
                k -= 1
            if k < 0:
                if nums[l] == 0:
                    k += 1
                l += 1    
            m = max(m,r - l +1)

        return m 
