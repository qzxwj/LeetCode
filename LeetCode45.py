class Solution(object):
    def jump(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        m = 0
        e = 0
        ans = 0
        for i in range(0, len(nums) - 1):
            m = max(m, nums[i] + i)
            if i == e:
                e = m
                ans += 1

        return ans