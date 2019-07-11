class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

class Solution:
    def isUnivalTree(self, root):
        self.check = True
        if root == None:
            return False
        self.val = root.val
        self._helper(root)
        return self.check

    def _helper(self, root):
        if root == None or self.check == False:
            return
        if root.val != self.val:
            self.check = False
        self._helper(root.left)
        self._helper(root.right)
    
if __name__ == "__main__":
    myTree = TreeNode(1)
    myTree.left = TreeNode(1)
    myTree.left.left = TreeNode(1)
    myTree.left.right = TreeNode(2)
    myTree.right = TreeNode(1)
    myTree.right.right = TreeNode(1)
    s = Solution()
    print(s.isUnivalTree(myTree))
    