class Solution:
    def thirdMax(self, nums: List[int]) -> int:
        h = []
        nums = set(nums)
        for num in nums:
            heappush(h, -num)
            # if (len(h) > 3):
            #     heappop(h)
        
        if len(h) >= 3:
            for _ in range(2):
                heappop(h)
        return -heappop(h)
