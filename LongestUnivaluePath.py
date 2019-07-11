class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def longestUnivaluePath(self, root):
        self.longest = 0
        self._helper(root, None)
        return self.longest
    def _helper(self, root, prevVal):
        if root == None: return 0
        l, r = self._helper(root.left, root.val), self._helper(root.right, root.val)
        self.longest = max(self.longest, l + r)
        return max(l, r) + 1 if root.val == prevVal else 0
        
if __name__ == "__main__":
    myTree = TreeNode(4)
    myTree.left = TreeNode(-7)
    myTree.right = TreeNode(-3)
    myTree.right.left = TreeNode(-9)
    myTree.right.right = TreeNode(-3)
    myTree.right.right.left = TreeNode(-4)
    s = Solution()
    print(s.longestUnivaluePath(myTree))        