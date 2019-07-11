class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

class Solution:
    def maxDepth(self, root):
        if root == None:
            return
        return self._helper(root)
    def _helper(self, root):
        if root == None:
            return 0
        l = self._helper(root.left)
        r = self._helper(root.right)
        return (max(l, r) + 1)

if __name__ == "__main__":
    myTree = TreeNode(3)
    myTree.left = TreeNode(9)
    myTree.right = TreeNode(20)
    myTree.right.left = TreeNode(15)
    myTree.right.right = TreeNode(7)
    s = Solution()
    print(s.maxDepth(myTree))