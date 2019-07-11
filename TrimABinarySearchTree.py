class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def trimBST(self, root, L, R):
        if root == None:
            return None
        return self._helper(root, L, R)
    def _helper(self, root, L, R):
        if root == None:
            return None
        if L > root.val:
            return self._helper(root.right, L, R)
        elif R < root.val:
            return self._helper(root.left, L, R)
        root.left = self._helper(root.left, L, R)
        root.right = self._helper(root.right, L, R)
        return root
