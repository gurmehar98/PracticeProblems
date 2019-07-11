class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def sumOfLeftLeaves(self, root):
        self.total = 0
        if root == None:
            return 0
        self._helper(root)
        return self.total
    def _helper(self, root):
        if root == None:
            return
        if root.left != None:
            if root.left.left == None and root.left.right == None:
                self.total += root.left.val
        self._helper(root.left)
        self._helper(root.right)
    
if __name__ == "__main__":
    myTree = TreeNode(3)
    myTree.left = TreeNode(9)
    myTree.right = TreeNode(20)
    myTree.right.left = TreeNode(15)
    myTree.right.right = TreeNode(7)
    s = Solution()
    print(s.sumOfLeftLeaves(myTree))