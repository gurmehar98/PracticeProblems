class Node(object):
    def __init__(self, val, children):
        self.val = val
        self.children = children

class Solution(object):
    def maxDepth(self, root):
        if root == None:
            return 0
        return(self._helper(root))
    def _helper(self, root):
        if root == None:
            return 0
        maxHeight = -float("inf")
        if root.children != None:    
            for c in root.children:
                height = self._helper(c)
                if maxHeight < height:
                    maxHeight = height
        if root.children == None or maxHeight == -float("inf"):
            return 1
        return (maxHeight + 1)
        
if __name__ == "__main__":
    n2 = Node(2, None)
    n4 = Node(4, None)
    n5 = Node(5, None)
    n6 = Node(6, None)
    n3 = Node(3, [n5, n6])
    n1 = Node(1, [n3, n2, n4])
    s = Solution()
    print(s.maxDepth(n1))