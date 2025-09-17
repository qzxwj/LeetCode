class Solution(object):
    def minSubArrayLen(self, target, nums):
        """
        :type target: int
        :type nums: List[int]
        :rtype: int
        """
        if sum(nums) < target:
            return 0

        l = len(nums)
        s = 0
        i = 0
        for j in range(len(nums)):
            s += nums[j]
            while s >= target:
                l = min(l, j + 1 - i)
                s -= nums[i]
                i += 1

        return l