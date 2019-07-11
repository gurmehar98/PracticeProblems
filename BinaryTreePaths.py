class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def binaryTreePaths(self, root):
        self.res = []
        self._helper(root, "")
        return self.res
    def _helper(self, root, pathStr):
        if root != None:
            if root.left == None and root.right == None: self.res.append(pathStr + str(root.val))
            else:
                self._helper(root.left, pathStr + str(root.val) + "->")
                self._helper(root.right, pathStr + str(root.val) + "->")

if __name__ == "__main__":
    myTree = TreeNode(1)
    myTree.left = TreeNode(2)
    myTree.left.right = TreeNode(5)
    myTree.right = TreeNode(3)
    s = Solution()
    print(s.binaryTreePaths(myTree))        