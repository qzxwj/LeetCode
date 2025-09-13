class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        curr = nums[0]
        ans = nums[0]
        for i in range(1, len(nums)):
            if curr <0:
                curr = nums[i]
            else:
                curr = curr + nums[i]
            ans = max(curr, ans)

        return ans