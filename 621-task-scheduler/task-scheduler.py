class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        count = {}
        for i in tasks:
            if i in count:
                count[i] += 1
            else:
                count[i] = 1
        
        maxheap = [-cnt for cnt in count.values()]
        heapq.heapify(maxheap)
        time = 0 
        q = deque()

        while maxheap or q:
            time += 1
            if maxheap:
                cnt = 1 + heapq.heappop(maxheap)
                if cnt:
                    q.append([cnt, time + n])
            if q and time == q[0][1]:
                heapq.heappush(maxheap, q.popleft()[0])
        
        return time