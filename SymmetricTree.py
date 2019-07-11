class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def isSymmetric(self, root):
        if root == None:
            return True
        return self._helper(root.left, root.right)
    def _helper(self, L, R):
        if L == None and R == None:
            return True
        if L == None or R == None:
            return False
        if L.val == R.val:
            return self._helper(L.left, R.right) and self._helper(L.right, R.left)
        else:
            return False

if __name__ == "__main__":
    myTree = TreeNode(1)
    myTree.left = TreeNode(2)
    myTree.left.left = TreeNode(3)
    myTree.left.right = TreeNode(4)
    myTree.right = TreeNode(2)
    myTree.right.left = TreeNode(4)
    myTree.right.right = TreeNode(3)
    s = Solution()
    print(s.isSymmetric(myTree))