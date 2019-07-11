class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def findTilt(self, root):
        if root == None: return 0
        self.res = 0
        self._helper(root)
        return self.res
    def _helper(self, root):
        if root == None: return 0
        left, right = self._helper(root.left), self._helper(root.right)
        self.res += abs(left - right)
        return root.val + left + right

if __name__ == "__main__":
    myTree = TreeNode(1)
    myTree.left = TreeNode(2)
    myTree.left.left = TreeNode(4)
    myTree.right = TreeNode(3)
    myTree.right.left = TreeNode(5)
    s = Solution()
    print(s.findTilt(myTree))        