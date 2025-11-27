class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        hmap = {}
        ans = []

        for i in nums:
            hmap[i] = 1 + hmap.get(i, 0)
        print(hmap)
        heap = []
        for num in hmap.keys():
            heapq.heappush(heap, [hmap[num], num])
            if len(heap) > k:
                heapq.heappop(heap)
        print(heap)
        for _ in range(len(heap)):
            ans.append(heapq.heappop(heap)[1])
        
        return ans