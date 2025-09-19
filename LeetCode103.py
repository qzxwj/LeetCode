# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
import collections

class Solution(object):
    def zigzagLevelOrder(self, root):
        if root is None:
            return []

        result = []
        queue = collections.deque([root])
        left_to_right = True

        while queue:
            level = []
            for _ in range(len(queue)):
                cur = queue.popleft()
                level.append(cur.val)
                if cur.left:
                    queue.append(cur.left)
                if cur.right:
                    queue.append(cur.right)
            if not left_to_right:
                level.reverse()
            result.append(level)
            left_to_right = not left_to_right  # 方向切换

        return result