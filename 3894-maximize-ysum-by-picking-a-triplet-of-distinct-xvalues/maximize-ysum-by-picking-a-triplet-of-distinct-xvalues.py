class Solution:
    def maxSumDistinctTriplet(self, x, y):
        hashMap = {}

        for xv, yv in zip(x, y):
            hashMap[xv] = max(hashMap.get(xv, 0), yv)
        
        if len(hashMap) < 3:
            return -1
        
        top3 = sorted(hashMap.values(), reverse=True)

        return top3[0] + top3[1] + top3[2]