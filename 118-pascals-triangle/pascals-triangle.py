class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        if numRows == 1:
            return [[1]]
        elif numRows ==2:
            return [[1],[1,1]]
        else:
            output = [[1],[1,1]]
            while numRows - 2 > 0:
                temp = []
                for i in range(len(output[-1])-1):
                    sm = output[-1][i] + output[-1][i+1]
                    temp.append(sm)
                temp.insert(0,1)
                temp.append(1)
                output.append(temp)
                numRows -= 1
        return output
