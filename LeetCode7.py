class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        if x ==0:
            return 0
        elif x > 0:
            a = int(str(x)[::-1])
        else:
            a = int('-' + str(x)[:0:-1])

        if a< (-2)**31 or a> (2**31-1):
            return 0

        return a