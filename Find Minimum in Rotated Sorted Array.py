class Solution:
    def findMin(self, nums: List[int]) -> int:

        res = nums[0] #taking res to compare and find min value from array

        #solving by binart search
        l , r = 0 , len(nums)- 1

        while l<=r:
            #chicking if the array is sorted than return the min first element
            if nums[l] < nums[r]:
                res = min(res,nums[l])
                break
            
            m = (l + r)//2
            res = min(res, nums[m]) 

            if nums[m] >= nums[l]: 
                l = m + 1
            else:
                r = m - 1
        return res
