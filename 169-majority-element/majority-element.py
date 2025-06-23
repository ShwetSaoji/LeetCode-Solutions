class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        maj = len(nums)/2

        hashMap = {}

        for i in nums:
            if i in hashMap:
                hashMap[i] += 1
                if hashMap[i] > maj:
                    return i
            else:
                hashMap[i] = 1