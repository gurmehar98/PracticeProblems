class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def hasPathSum(self, root, sum):
        self.check = False
        self._helper(root, sum)
        return self.check
    def _helper(self, root, sum):
        if root == None: return
        if root.val == sum and root.left == None and root.right == None: self.check = True
        self._helper(root.left, sum - root.val)
        self._helper(root.right, sum - root.val)