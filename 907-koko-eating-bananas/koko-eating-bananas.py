class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l , r = 1 , max(piles)
        res = r
        while l <= r:
            m = (l+r)//2
            print(m)
            tot_time = 0
            for i in piles:
                tot_time += ceil(i/m)
            if tot_time <= h:
                res = m 
                r = m - 1
            else:
                l = m + 1

        return res