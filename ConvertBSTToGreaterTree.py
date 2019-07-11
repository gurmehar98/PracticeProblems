class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def convertBST(self, root):
        self.total = 0
        if root == None:
            return None
        return(self._helper(root))
    def _helper(self, root):
        if root == None:
            return 0
        self._helper(root.right)
        self.total += root.val
        root.val = self.total
        self._helper(root.left)
        return root

if __name__ == "__main__":
    myTree = TreeNode(5)
    myTree.left = TreeNode(2)
    myTree.right = TreeNode(13)
    s = Solution()
    print(s.convertBST(myTree))