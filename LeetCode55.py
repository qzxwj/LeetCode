class Solution(object):
    def canJump(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        m = 0
        for i, x in enumerate(nums):
            if i <= m:
                m = max(m, i+x)
        return m >=len(nums) - 1