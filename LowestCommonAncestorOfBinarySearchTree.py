class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def lowestCommonAncestor(self, root, p, q):
        return self._helper(root, p, q)
    def _helper(self, root, p, q):
        if root == None: return None
        if root.val > p.val and root.val > q.val: return self._helper(root.left, p, q)
        elif root.val < p.val and root.val < q.val: return self._helper(root.right, p, q)
        else: return root
        