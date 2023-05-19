class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        m = max(candies)
        res = []
        for i in candies:
            if i + extraCandies >= m:
                print(i + extraCandies)
                res.append(True)
            else:
                print(i + extraCandies)
                res.append(False)
        
        return res
