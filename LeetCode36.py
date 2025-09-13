class Solution(object):
    def isValidSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: bool
        """
        m = len(board)   #行数
        n = len(board[0])   #列数

        r = [set() for _ in range(m)]
        c = [set() for _ in range(n)]
        t = [[set() for _ in range(m//3)] for _ in range(n//3)]

        for i in range(m):
            for j in range(n):
                if board[i][j] != '.':
                    if board[i][j] in r[i] or board[i][j] in c[j] or board[i][j] in t[i//3][j//3]:
                        return False

                    r[i].add(board[i][j])
                    c[j].add(board[i][j])
                    t[i//3][j//3].add(board[i][j])

        return True