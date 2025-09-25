# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution(object):
    def buildTree(self, preorder, inorder):
        """
        :type preorder: List[int]
        :type inorder: List[int]
        :rtype: Optional[TreeNode]
        """

        pos = dict()
        n = len(preorder)

        def build(preorder, inorder, pl, pr, il, ir):
            if pl > pr or il > ir:
                return None

            k = pos[preorder[pl]] - il

            root = TreeNode(preorder[pl])

            root.left = build(preorder, inorder, pl + 1, pl + k, il, il + k - 1)
            root.right = build(preorder, inorder, pl + k + 1, pr, il + k + 1, ir)

            return root

        for i in range(0, n):
            pos[inorder[i]] = i

        return build(preorder, inorder, 0, n - 1, 0, n - 1)