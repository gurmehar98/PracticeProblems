class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def findTarget(self, root, k):
        self.checkSet = set()
        if root == None:
            return None
        return self._helper(root, k)
    def _helper(self, root, k):
        if root == None:
            return False
        comp = k - root.val
        if comp in self.checkSet:
            return True
        self.checkSet.add(root.val)
        return self._helper(root.left, k) or self._helper(root.right, k)

if __name__ == "__main__":
    myTree = TreeNode(5)
    myTree.left = TreeNode(3)
    myTree.left.left = TreeNode(2)
    myTree.left.right = TreeNode(4)
    myTree.right = TreeNode(6)
    myTree.right.right = TreeNode(7)
    s = Solution()
    print(s.findTarget(myTree, 9))