class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        # ans = []
        hmap = {}

        for i in range(len(numbers)):
            diff = target - numbers[i]
            if diff in hmap:
                return [hmap[diff]+1, i+1]
            else:
                hmap[numbers[i]] = i
        

        
        
        