class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def insertIntoBST(self, root, val):
        if root == None:
            return None
        return self._helper(root, val)
    def _helper(self, root, val):
        if root == None:
            return TreeNode(val)
        if val < root.val:
            root.left = self._helper(root.left, val)
        else:
            root.right = self._helper(root.right, val)
        return root

if __name__ == "__main__":
    myTree = TreeNode(4)
    myTree.left = TreeNode(2)
    myTree.left.left = TreeNode(1)
    myTree.left.right = TreeNode(3)
    myTree.right = TreeNode(7)
    s = Solution()
    print(s.insertIntoBST(myTree, 5))