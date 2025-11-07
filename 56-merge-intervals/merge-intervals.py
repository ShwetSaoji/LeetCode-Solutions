class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        res = []
        intervals = sorted(intervals, key = lambda i:i[0])
        print(intervals)
        res.append(intervals[0])

        for i in range(1, len(intervals)):
            if res[-1][1] < intervals[i][0]:
                res.append(intervals[i])
            else:
                minStart = min(res[-1][0], intervals[i][0])
                maxEnd = max(res[-1][1], intervals[i][1])
                res[-1] = [minStart, maxEnd]
        
        return res
        # for i in range(len(intervals)):
            