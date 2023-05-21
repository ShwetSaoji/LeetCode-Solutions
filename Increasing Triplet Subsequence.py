class Solution:
    def increasingTriplet(self, nums: List[int]) -> bool:

        f = math.inf
        s = math.inf

        for i in nums:
            if i > s:
                return True
            if i > f:
                s = min(s,i)
            else:
                f = min(f,i)
        
        return False
