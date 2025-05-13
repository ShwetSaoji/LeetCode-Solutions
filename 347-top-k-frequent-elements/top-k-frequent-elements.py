class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        hashMap = {}

        for i in nums:
            hashMap[i] = hashMap.get(i, 0) + 1
        
        hashMap = dict(sorted(hashMap.items(), key=lambda i:i[1], reverse=True))

        ans = []
        for i, v in hashMap.items():
            if k <= 0:
                break
            else:
                ans.append(i)
                k -= 1
        return ans 