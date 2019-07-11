class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def increasingBST(self, root):
        self.finalList = []
        if root == None:
            return None
        self._helper(root)
        res = curr = TreeNode(None)
        for elements in self.finalList:
           curr.right = TreeNode(elements)
           curr = curr.right
        return res.right 
    def _helper(self, root):
        if root == None:
            return None
        self._helper(root.left)
        self.finalList.append(root.val)
        self._helper(root.right)

if __name__ == "__main__":
    myTree = TreeNode(5)
    myTree.left = TreeNode(3)
    myTree.left.left = TreeNode(2)
    myTree.left.left.left = TreeNode(1)
    myTree.left.right = TreeNode(4)
    myTree.right = TreeNode(6)
    myTree.right.right = TreeNode(8)
    myTree.right.right.left = TreeNode(7)
    myTree.right.right.right = TreeNode(9)
    s = Solution()
    print(s.increasingBST(myTree))