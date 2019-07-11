class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

class Solution:
    def findSecondMinimumValue(self, root):
        self.min1 = float("inf")
        self.min2 = float("inf")
        if root == None:
            return None
        self._helper(root)
        if self.min2 == float("inf"):
            return -1
        return self.min2
    def _helper(self, root):
        if root == None:
            return None
        self._helper(root.left)
        self._helper(root.right)
        if self.min1 > root.val and self.min2 > root.val:
            self.min2 = self.min1
            self.min1 = root.val
        elif self.min1 < root.val and self.min2 > root.val:
            self.min2 = root.val

if __name__ == "__main__":
    myTree = TreeNode(2)
    myTree.left = TreeNode(2)
    myTree.right = TreeNode(5)
    myTree.right.left = TreeNode(5)
    myTree.right.right = TreeNode(7)
    s = Solution()
    print(s.findSecondMinimumValue(myTree))