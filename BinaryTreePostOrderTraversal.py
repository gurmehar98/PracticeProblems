class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    #iterative Solution
    def postorderTraversal(self, root):
        resList, stack = [], [root]
        while stack:
            node = stack.pop()
            if node:
                resList.append(node.val)
                stack.append(node.left)
                stack.append(node.right)
        return resList[::-1]

    #Recursive Solution
    '''
    def postorderTraversal(self, root):
        self.resList = []
        self._helper(root)
        return self.resList
    def _helper(self, root):
        if root == None: return None
        self._helper(root.left)
        self._helper(root.right)
        self.resList.append(root.val)
    '''