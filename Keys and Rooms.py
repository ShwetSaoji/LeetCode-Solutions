class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        visited = [False] * len(rooms)
        visited[0] = True
        stack = [0]

        while stack:
            key = stack.pop()
            for i in rooms[key]:
                if not visited[i]:
                    visited[i] = True
                    stack.append(i)
        
        return all(visited)
