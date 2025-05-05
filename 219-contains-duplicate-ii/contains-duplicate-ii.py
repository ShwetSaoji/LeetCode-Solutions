class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        hm = {}

        for i, n in enumerate(nums):
            if n in hm:
                hm[n].append(i)
            else:
                hm[n] = [i]
        
        for item, value in hm.items():
            if len(value) < 2:
                continue
            else:
                for i in range(len(value)-1):
                    if value[i+1] - value[i] <= k:
                        return True
        
        return False
