class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        # nums = [-num for num in nums]
        heapq.heapify(nums)

        while len(nums) > k:
            heapq.heappop(nums)
        
        return  nums[0]