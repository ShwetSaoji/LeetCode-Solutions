class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        k = 1
        mx = 0
        left = 0

        for right, val  in enumerate(nums):
            if val == 0:
                k-=1
            if k < 0:
                if nums[left] == 0:
                    k+=1
                left += 1
            mx = max(mx, right - left)
        
        return mx
