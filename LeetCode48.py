class Solution(object):
    def rotate(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: None Do not return anything, modify matrix in-place instead.
        """
        n = len(matrix)

        for i in range(0, n):
            for j in range(0, i):
                matrix[j][i], matrix[i][j] = matrix[i][j], matrix[j][i]

        for i in range(0, n):
            for j in range(0, n // 2):
                matrix[i][n - j - 1], matrix[i][j] = matrix[i][j], matrix[i][n - j - 1]

        return matrix