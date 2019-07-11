class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def tree2str(self, t):
        if t == None:
            return ""
        return self._helper(t)
    def _helper(self, t):
        if t == None:
            return ""
        res = str(t.val)
        if t.left:
            res += "(" + self._helper(t.left) + ")"
            if t.right:
                res += "(" + self._helper(t.right) + ")"
        elif t.right:
            res += "()" + "(" + self._helper(t.right) + ")"
        return res

if __name__ == "__main__":
    myTree = TreeNode(1)
    myTree.left = TreeNode(2)
    myTree.left.left = TreeNode(4)
    myTree.right = TreeNode(3)
    s = Solution()
    print(s.tree2str(myTree))