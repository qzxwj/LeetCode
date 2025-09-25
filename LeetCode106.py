# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution(object):
    def buildTree(self, inorder, postorder):
        """
        :type inorder: List[int]
        :type postorder: List[int]
        :rtype: Optional[TreeNode]
        """

        def build(inorder, postorder):
            if len(postorder) == 0:
                return None

            node = TreeNode(postorder[-1])
            i = inorder.index(postorder[-1])

            node.left = build(inorder[:i], postorder[:i])
            node.right = build(inorder[i + 1:], postorder[i:-1])

            return node

        return build(inorder, postorder)