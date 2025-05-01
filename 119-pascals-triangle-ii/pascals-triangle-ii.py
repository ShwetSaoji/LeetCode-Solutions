class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        if rowIndex == 0:
            return [1]
        elif rowIndex == 1:
            return [1,1]
        else:
            output = [[1],[1,1]]
            while rowIndex - 1 > 0:
                temp = []
                for i in range(len(output[-1])-1):
                    sm = output[-1][i] + output[-1][i+1]
                    temp.append(sm)
                temp.insert(0,1)
                temp.append(1)
                output.append(temp)
                rowIndex -= 1
        return output[-1]