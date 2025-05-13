class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        hashMap = {}

        for i in nums:
            hashMap[i] = hashMap.get(i, 0) + 1
        
        heap = []

        for item, value in hashMap.items():
            heapq.heappush(heap, (value, item))
            if len(heap) > k:
                heapq.heappop(heap)
        res = []
        for i in heap:
            res.append(i[1])
        return res