class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        visit = set()
        # directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        islands = 0 

        def dfs(r, c):
            if r < 0 or r >= len(grid) or c < 0 or c >= len(grid[0]) or grid[r][c] == "0" or (r, c) in visit:
                return
            visit.add((r, c))
            return (dfs(r + 1, c),
            dfs(r - 1, c),
            dfs(r, c + 1),
            dfs(r, c - 1))       

        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if (i, j) not in visit and grid[i][j] == "1":
                    dfs(i, j)
                    islands += 1
        
        return islands
