class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def flatten(self, root):
        if root == None: return None
        self._helper(root)
    def _helper(self, root):
        if root == None: return None
        self._helper(root.left)
        self._helper(root.right)
        temp = root.left
        if temp == None: return
        while temp.right != None: temp = temp.right
        temp.right = root.right
        root.right = root.left
        root.left = None

if __name__ == "__main__":
    myTree = TreeNode(1)
    myTree.left = TreeNode(2)
    myTree.left.left = TreeNode(3)
    myTree.left.right = TreeNode(4)
    myTree.right = TreeNode(5)
    myTree.right.right = TreeNode(6)
    s = Solution()
    print(s.flatten(myTree))