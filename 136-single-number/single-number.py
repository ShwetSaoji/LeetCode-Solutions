class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        hm = {}

        for i in nums:
            
            if i in hm:
                hm[i]+= 1
            else:
                hm[i] = 1
        
        for i, v in hm.items():
            if v == 1:
                return i 
        