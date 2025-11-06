class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        res = [] 
        intervals = sorted(intervals, key=lambda i: i[0])
        res.append(intervals[0])

        for i in range(1, len(intervals)):
            if intervals[i][0] > res[-1][1]:
                res.append(intervals[i])
            else:
                new_start = min(res[-1][0], intervals[i][0])
                new_end = max(res[-1][1], intervals[i][1])
                res[-1] = [new_start, new_end]
        return res

        # for i in range(len(intervals)):
            