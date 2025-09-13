class Solution(object):
    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """
        n = len(digits)
        if n == 0:
            return []

        li = []
        path = [0] * n
        d = {'2': 'abc', '3': 'def', '4': 'ghi', '5': 'jkl', '6': 'mno', '7': 'pqrs', '8': 'tuv', '9': 'wxyz'}

        def dfs(i):
            if i == n:
                li.append("".join(path))
                return

            for s in d[digits[i]]:
                path[i] = s
                dfs(i + 1)

        dfs(0)
        return li