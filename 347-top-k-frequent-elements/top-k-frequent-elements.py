class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        hmap = {}
        ans = []

        for i in nums:
            hmap[i] = 1 + hmap.get(i, 0)
        
        hmap = sorted(hmap.items(), key=lambda i : i[1], reverse=True)[:k]
        # print(hmap)
        for i in hmap:
            ans.append(i[0])
        
        return ans