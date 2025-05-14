class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums=sorted(nums)
        res = []
        for i in range(len(nums)-2):
            l, r  = i+1, len(nums)-1
            while l < r:
                threesom = nums[i] + nums[l] + nums[r]
                if threesom > 0:
                    r -= 1
                elif threesom < 0:
                    l += 1
                else:
                    res.append((nums[i], nums[l], nums[r]))
                    l += 1
                    r -= 1
        ans = []
        
        
        for i in list(set(res)):
            ans.append(list(i))
        return ans
