class Solution:
    def rob(self, nums: List[int]) -> int:
        
        if len(nums) <= 1:
            return nums[0]
        elif len(nums) == 2:
            return max(nums[0] , nums[1])
        
        
        #return max(self.abc(nums[1:]), self.abc(nums[:-1]))
        return max(self.abc(nums[1:]), self.abc(nums[:-1]))
    def abc(self, arr: List[int]) -> int:
        dp = [0] * len(arr)
        print(dp)
        dp[0] = arr[0]
        dp[1] = max(arr[0], arr[1])
        for i in range(2, len(arr)):
            dp[i] = max(dp[i-1], arr[i]+dp[i-2])
            print(dp)
        return dp[-1]  
