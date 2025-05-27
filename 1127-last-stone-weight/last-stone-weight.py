class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        stones = [-i for i in stones]
        heapq.heapify(stones)
        while len(stones) > 1:
            largest = heapq.heappop(stones)
            large = heapq.heappop(stones)
            if large > largest:
                heapq.heappush(stones, largest - large)
            
        print(stones)
        if len(stones) == 0:
            return 0 
        else:
            return abs(stones[0])