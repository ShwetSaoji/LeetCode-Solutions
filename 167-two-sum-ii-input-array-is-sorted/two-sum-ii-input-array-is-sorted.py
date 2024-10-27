class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        hmap = {}

        for i, n in enumerate(numbers):
            diff = target - n
            if diff in hmap:
                return [hmap[diff]+1, i+1]
            else:
                hmap[n] = i
        
        