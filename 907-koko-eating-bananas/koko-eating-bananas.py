class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l , r = 1, max(piles)
        res = 0 
        while l <= r:
            k = (r+l)//2
            tot_h = 0
            for i in piles:
                tot_h += ceil(i/k)
            if tot_h > h:
                l = k + 1
            else:
                res = k 
                r = k - 1
        
        return res
        
        # l , r = 1 , max(piles)
        # res = r
        # while l <= r:
        #     m = (l+r)//2
        #     print(m)
        #     tot_time = 0
        #     for i in piles:
        #         tot_time += ceil(i/m)
        #     if tot_time <= h:
        #         res = m 
        #         r = m - 1
        #     else:
        #         l = m + 1

        # return res