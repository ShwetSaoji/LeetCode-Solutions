class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        l , r = 0 , len(matrix)-1

        while l <= r:
            target_row = (l+r)//2
            if target < matrix[target_row][0]:
                r = target_row -1
            elif target > matrix[target_row][-1]:
                l = target_row + 1
            else:
                break
        row = matrix[target_row]
        l , r = 0 , len(row) - 1
        while l <= r:
            m = (l + r)//2
            if target == row[m]:
                return True
            elif target > row[m]:
                l = m + 1
            else:
                r = m - 1
        return False
        