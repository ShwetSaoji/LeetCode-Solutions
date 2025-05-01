class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        # for i in range(len(nums)):
        #     for j in range(i+1, len(nums)):
        #         if nums[i] == nums[j] and j - i <= k:
        #             return True
        # return False

        hm = {}
        for i, n in enumerate(nums):
            if n not in hm:
                hm[n] = [i]
            else:
                hm[n].append(i)
        print(hm)
        for key, value in hm.items():
            if len(value) < 2:
                continue
            else:
                for i in range(len(value)-1):
                    if abs(value[i] - value[i+1]) <= k:
                        return True
        return False