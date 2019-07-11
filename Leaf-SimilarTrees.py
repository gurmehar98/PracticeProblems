class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def leafSimilar(self, root1, root2):
        self.list1 = []
        self.list2 = []
        if root1 and root2:
            self._helper(root1, 1)
            self._helper(root2, 2)
            return (self.list1 == self.list2)
        else:
            return False
    def _helper(self, root, n):
        if root:
            self._helper(root.left, n)
            self._helper(root.right, n)
            if root.left == None and root.right == None and n == 1:
                self.list1.append(root.val)
            elif root.left == None and root.right == None and n == 2:
                self.list2.append(root.val)