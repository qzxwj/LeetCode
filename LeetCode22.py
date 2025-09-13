class Solution(object):
    def generateParenthesis(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        ans = []

        def f(l, r, x):
            if l + r == 0:
                ans.append(x)
                return

            if l:
                f(l - 1, r, x + "(")
            if r > l:
                f(l, r - 1, x + ")")

        f(n, n, "")
        return ans