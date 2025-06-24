class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        hashMap = {}

        for i in nums:
            hashMap[i] = 1 + hashMap.get(i, 0)
        ans = []
        for num, count in hashMap.items():
            if count > len(nums)/3:
                ans.append(num)
        
        return ans