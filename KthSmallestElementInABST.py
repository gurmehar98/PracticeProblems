class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def kthSmallest(self, root, k):
        self.inOrderList = []
        self._helper(root, k)
        return self.inOrderList[k - 1]
    def _helper(self, root, k):
        if root == None: return None
        self._helper(root.left, k)
        self.inOrderList.append(root.val)
        self._helper(root.right, k)