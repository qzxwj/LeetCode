# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def inorderTraversal(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: List[int]
        """
        li = []

        def f(root):
            if root is None:
                return
            f(root.left)
            li.append(root.val)
            f(root.right)

        f(root)
        return li