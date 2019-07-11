from collections import deque
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def levelOrderBottom(self, root):
        if root == None:
            return []
        return self._helper(root)
    def _helper(self, root):
        finalList = []
        if root == None:
            return None
        myQueue = deque()
        myQueue.append(root)
        while(myQueue):
            queueSize = len(myQueue)
            currList = []
            while(queueSize > 0):
                curr = myQueue.popleft()
                currList.append(curr.val)
                if curr.left != None:
                    myQueue.append(curr.left)
                if curr.right != None:
                    myQueue.append(curr.right)
                queueSize -= 1
            finalList.append(currList)
        return finalList[::-1]
        

if __name__ == "__main__":
    myTree = TreeNode(3)
    myTree.left = TreeNode(9)
    myTree.right = TreeNode(20)
    myTree.right.left = TreeNode(15)
    myTree.right.right = TreeNode(7)
    s = Solution()
    print(s.levelOrderBottom(myTree))