class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def maxPathSum(self, root):
        self.maxSum = 0
        self._helper(root)
        return self.maxSum
    def _helper(self, root):
        if root == None: return 0
        l = self._helper(root.left)
        r = self._helper(root.right)
        self.maxSum = max(self.maxSum, l + root.val + r)
        return max(l, r) + root.val