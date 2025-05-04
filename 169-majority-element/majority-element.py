class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        hm = defaultdict(int)

        for i in nums:
            hm[i] += 1
        
        for i , v in hm.items():
            if v > (len(nums)/2):
                return i 
