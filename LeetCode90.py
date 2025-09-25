class Solution(object):
    def subsetsWithDup(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        nums.sort()    # 很关键，必须
        n = len(nums)
        ans = set()

        for i in range(0, 1 << n):
            subset = []
            for j in range(0, n):
                if i & (1 << j):
                    subset.append(nums[j])
            ans.add(tuple(subset))

        return [list(t) for t in ans] 