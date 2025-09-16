class Solution(object):
    def exist(self, board, word):
        """
        :type board: List[List[str]]
        :type word: str
        :rtype: bool
        """
        m, n = len(board), len(board[0])
        visit = [[False for _ in range(n)] for _ in range(m)]

        def dfs(word, row, col, index):
            if index == len(word):
                return True

            if row >= m or row < 0 or col >= n or col < 0 or board[row][col] != word[index] or visit[row][col]:
                return False

            visit[row][col] = True
            r = False
            r |= dfs(word, row + 1, col, index + 1)
            r |= dfs(word, row, col + 1, index + 1)
            r |= dfs(word, row - 1, col, index + 1)
            r |= dfs(word, row, col - 1, index + 1)
            visit[row][col] = False
            return r

        for i in range(m):
            for j in range(n):
                if dfs(word, i, j, 0):
                    return True

        return False