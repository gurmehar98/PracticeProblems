class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    #Iterative Solution
    def preorderTraversal(self, root):
        resList, stack = [], [root]
        while stack:
            node = stack.pop()
            if node:
                resList.append(node.val)
                stack.append(node.right)
                stack.append(node.left)
        return resList

    #Recursive Solution
    '''
    def preorderTraversal(self, root):
        self.resList = []
        self._helper(root)
        return self.resList
    def _helper(self, root):
        if root == None: return None
        self.resList.append(root.val)
        self._helper(root.left)
        self._helper(root.right)
    '''