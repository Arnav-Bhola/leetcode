class Solution(object):
    def generate(self, numRows):
        """
        :type numRows: int
        :rtype: List[List[int]]
        """
        
        if numRows == 1:
            return [[1]]
        if numRows == 2:
            return [[1], [1,1]]

        solution = [[1], [1,1]]
        numRows -= 2
        while numRows > 0:
            rowAbove = solution[-1]
            newRow = [1]
            for index in range(len(rowAbove) - 1):
                newRow.append(rowAbove[index] + rowAbove[index+1])
            newRow.append(1)
            solution.append(newRow)
            numRows -= 1
        return solution
