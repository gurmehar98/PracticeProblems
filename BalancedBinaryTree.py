class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def isBalanced(self, root):
        self.check = True
        self._helper(root)
        return self.check
    def _helper(self, root):
        if root == None: return 0
        l = self._helper(root.left)
        r = self._helper(root.right)
        if abs(l - r) > 1: self.check = False
        return max(l, r) + 1

if __name__ == "__main__":
    myTree = TreeNode(3)
    myTree.left = TreeNode(9)
    myTree.right = TreeNode(20)
    myTree.right.left = TreeNode(15)
    myTree.right.right = TreeNode(7)
    s = Solution()
    print(s.isBalanced(myTree))