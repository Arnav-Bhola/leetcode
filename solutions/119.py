class Solution(object):
    def getRow(self, rowIndex):
        """
        :type rowIndex: int
        :rtype: List[int]
        """
        
        rowIndex += 1
        if rowIndex == 1:
            return [1]
        if rowIndex == 2:
            return [1,1]

        solution = [[1], [1,1]]
        rowIndex -= 2
        while rowIndex > 0:
            rowAbove = solution[-1]
            newRow = [1]
            for index in range(len(rowAbove) - 1):
                newRow.append(rowAbove[index] + rowAbove[index+1])
            newRow.append(1)
            solution.append(newRow)
            rowIndex -= 1
        return solution[-1]
