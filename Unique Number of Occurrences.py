class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        
        dc = {}
        for i in arr:
            if i not in dc:
                dc[i] = 1
            else:
                dc[i] += 1
        return len(set(dc.values())) == len(set(arr))
