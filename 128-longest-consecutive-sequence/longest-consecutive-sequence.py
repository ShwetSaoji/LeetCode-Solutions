class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numSet = set(nums)
        ans = 0 
        for i in numSet:
            if not (i-1) in numSet:
                streak = 1 
                while (i+streak) in numSet:
                    streak += 1
                ans = max(ans, streak)
        return ans