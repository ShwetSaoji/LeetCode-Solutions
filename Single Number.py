class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        
        #nums.sort()
        #print(nums)
        dic = {}
        for i in nums:
            if i not in dic:
                dic[i] = 1
            else:
                dic[i] = dic[i] + 1
        
        return min(dic, key=dic.get)
