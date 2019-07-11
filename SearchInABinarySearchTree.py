class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

class Solution:
    def searchBST(self, root, val):
        self.searchVal = None
        if root == None:
            return None
        self._helper(root, val)
        return self.searchVal
    def _helper(self, root, val):
        if root == None:
            return None 
        if val < root.val:
            self._helper(root.left, val)
        elif val > root.val:
            self._helper(root.right, val)
        else:
            self.searchVal = root

if __name__ == "__main__":
    myTree = TreeNode(4)
    myTree.left = TreeNode(2)
    myTree.left.left = TreeNode(1)
    myTree.left.right = TreeNode(3)
    myTree.right = TreeNode(7)
    s = Solution()
    print(s.searchBST(myTree, 2))