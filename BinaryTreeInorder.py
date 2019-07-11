class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    #Iterative Solution
    def inorderTraversal(self, root):
        resList, stack = [], []
        while root or stack:
            if root:
                stack.append(root)
                root = root.left
            else:
                node = stack.pop()
                resList.append(node.val)
                root = node.right
        return resList

    #Recursive Solution
    '''
    def inorderTraversal(self, root):
        self.resList = []
        self._helper(root)
        return self.resList
    def _helper(self, root):
        if root == None: return None
        self._helper(root.left)
        self.resList.append(root.val)
        self._helper(root.right)
    '''

if __name__ == "__nain__":
    myTree = TreeNode(1)
    myTree.right = TreeNode(2)
    myTree.right.left = TreeNode(3)
    s = Solution()
    print(s.inorderTraversal(myTree))