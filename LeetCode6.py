class Solution(object):
    def convert(self, s, numRows):
        """
        :type s: str
        :type numRows: int
        :rtype: str
        """
        if numRows == 1:
            return s

        s1 = [''] * numRows
        for i, x in enumerate(s):
            j = i % (2 * numRows - 2)
            if j < numRows:
                s1[j] += x

            else:
                s1[-(j - numRows + 2)] += x

        s2 = ''
        for x in s1:
            s2 += x

        return s2