class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # hashSet = {}

        # for i in nums:
        #     if i in hashSet:
        #         hashSet[i] += 1
        #     else:
        #         hashSet[i] = 1
        
        # print(hashSet.items())
        # # arr = sorted(hashSet.items(), key = lambda it: it[1], reverse=True)
        # # arr = list(map(lambda it: it[0], arr))
        # # return arr[:k]

        # arr = dict(sorted(hashSet.items(), key = lambda x : x[1], reverse=True))
        # print(arr)
        # return list(arr.keys())[:k]

        hashSet = {}
        res = []
        for i in nums:
            if i in hashSet:
                hashSet[i] += 1
            else:
                hashSet[i] = 1
        
        for key, value in hashSet.items():
            heapq.heappush(res, [value, key])
            if len(res) > k:
                heapq.heappop(res)
        
        return [x for _, x in res]