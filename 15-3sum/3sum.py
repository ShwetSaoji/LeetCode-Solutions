class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = []
        nums.sort()

        for i, n in enumerate(nums):
            l, r = i+1 , len(nums)-1
            # if n > 0:
            #     break
            if i > 0 and n == nums[i-1]:
                continue
            while l < r:
                threesom = n + nums[l] + nums[r]

                if threesom > 0:
                    r -= 1
                elif threesom < 0:
                    l += 1
                else:
                    res.append([n, nums[l], nums[r]])
                    l += 1
                    r -= 1
                    while nums[l-1] == nums[l] and l < r:
                        l += 1                
        return res

        
                