class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Codec:
    def serialize(self, root):
        self.serializedValues = []
        self._helper1(root)
        return self.serializedValues
    def _helper1(self, root):
        if root:
            self.serializedValues.append(str(root.val))
            self._helper1(root.left)
            self._helper1(root.right)
        else: self.serializedValues.append("null")
    def deserialize(self, data):
        if data == []: return None
        self.index, root = 0, None
        return self._helper2(data, root)
    def _helper2(self, data, root):
        if self.index >= len(data) or data[self.index] == "null":
            self.index += 1
            return None
        root = TreeNode(data[self.index])
        self.index += 1
        root.left = self._helper2(data, root.left)
        root.right = self._helper2(data, root.right)
        return root

# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.deserialize(codec.serialize(root))

if __name__ == "__main__":
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(3)
    root.right.left = TreeNode(4)
    root.right.right = TreeNode(5)
    codec = Codec()
    print(codec.serialize(root))