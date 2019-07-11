class Node(object):
    def __init__(self, val, children):
        self.val = val
        self.children = children

class Solution(object):
    def postorder(self, root):
        self.finalList = []
        if root == None:
            return []
        self._helper(root)
        return self.finalList
    def _helper(self, root):
        if root == None:
            return
        if root.children != None:
            for c in root.children:
                self._helper(c)
        self.finalList.append(root.val)   

if __name__ == "__main__":
    n2 = Node(2, None)
    n4 = Node(4, None)
    n5 = Node(5, None)
    n6 = Node(6, None)
    n3 = Node(3, [n5, n6])
    n1 = Node(1, [n3, n2, n4])
    s = Solution()
    print(s.postorder(n1))