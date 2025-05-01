class Solution:
    def canAttendMeetings(self, intervals: List[List[int]]) -> bool:
        sortarr = sorted(intervals, key = lambda i : i[0])
        
        for i in range(1, len(intervals)):
            if sortarr[i][0] < sortarr[i-1][1]:
                return False
        return True