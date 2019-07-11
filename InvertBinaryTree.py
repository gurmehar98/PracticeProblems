class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def invertTree(self, root):
        if root == None:
            return None
        return self._helper(root)
    def _helper(self, root):
        if root == None:
            return None
        self._helper(root.left)
        self._helper(root.right)
        if root.left != None and root.right != None:
            temp = root.left
            root.left = root.right
            root.right = temp
        return root