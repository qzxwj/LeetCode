class Solution(object):
    def subsets(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        ans = []
        subset = []

        def dfs(nums, idx):
            if idx == len(nums):
                ans.append(list(subset))
                return

            subset.append(nums[idx])
            dfs(nums, idx + 1)

            subset.pop()
            dfs(nums, idx + 1)

        dfs(nums, 0)
        return ans