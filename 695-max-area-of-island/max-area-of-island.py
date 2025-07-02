class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]
        area = 0 
        row_len = len(grid)
        col_len = len(grid[0])
        visited = set()

        def dfs(r, c):
            if r < 0 or c < 0 or r >= row_len or c >= col_len or grid[r][c] == 0 or (r, c) in visited:
                return 0
            visited.add((r, c))
            return (1 + dfs(r + 1, c) + 
                        dfs(r - 1, c) + 
                        dfs(r, c + 1) +
                        dfs(r, c - 1))
            return area
 

        for i in range(row_len):
            for j in range(col_len):
                if grid[i][j] == 1:
                    area = max(area, dfs(i, j))
        
        return area



    #     class Solution:
    # def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
    #     ROWS, COLS = len(grid), len(grid[0])
    #     visit = set()

    #     def dfs(r, c):
    #         if (r < 0 or r == ROWS or c < 0 or
    #             c == COLS or grid[r][c] == 0 or
    #             (r, c) in visit
    #         ):
    #             return 0
    #         visit.add((r, c))
    #         return (1 + dfs(r + 1, c) + 
    #                     dfs(r - 1, c) + 
    #                     dfs(r, c + 1) + 
    #                     dfs(r, c - 1))

    #     area = 0
    #     for r in range(ROWS):
    #         for c in range(COLS):
    #             area = max(area, dfs(r, c))
    #     return area







