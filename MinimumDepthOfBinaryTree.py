class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def minDepth(self, root):
        return self._helper(root)
    def _helper(self, root):
        if root == None: return 0
        l = self._helper(root.left)
        r = self._helper(root.right)
        if root.right == None and root.left != None: return l + 1
        elif root.left == None and root.right != None: return r + 1
        else: return (min(l, r) + 1)

if __name__ == "__main__":
    myTree = TreeNode(1)
    myTree.left = TreeNode(2)
    s = Solution()
    print(s.minDepth(myTree))