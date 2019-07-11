class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def diameterOfBinaryTree(self, root):
        if root == None: return 0
        return self._helper(root)
    def _helper(self, root):
        if root == None: return 0
        maxDepth = 0
        l, r = self._helper(root.left), self._helper(root.right)
        maxDepth = max(maxDepth, l + r)
        return maxDepth + 1