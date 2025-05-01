class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        hp = {}

        for i in nums:
            if i in hp:
                hp[i] += 1
            else:
                hp[i] = 1
        
        for item, value in hp.items():
            if value > len(nums)//2:
                return item