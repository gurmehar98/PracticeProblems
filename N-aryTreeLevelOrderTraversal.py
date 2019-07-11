from collections import deque
class Node:
    def __init__(self, val, children):
        self.val = val
        self.children = children

class Solution(object):
    def levelOrder(self, root):
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
                for c in curr.children:
                    myQueue.append(c)
                queueSize -= 1
            finalList.append(currList)
        return finalList