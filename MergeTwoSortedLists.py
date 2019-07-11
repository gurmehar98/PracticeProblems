class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None
        
class Solution:
    def mergeTwoLists(self, l1, l2):
        self.resList = None
        while l1 and l2:
            if l1.val > l2.val:
                self._addNode(l2.val)
                l2 = l2.next
            else:
                self._addNode(l1.val)
                l1 = l1.next
        while l1:
            self._addNode(l1.val)
            l1 = l1.next
        while l2:
            self._addNode(l2.val)
            l2 = l2.next
        return self.resList
    def _addNode(self, val):
        if self.resList == None:
            self.resList = ListNode(val)
            return
        temp = self.resList
        while temp.next != None:
             temp = temp.next
        temp.next = ListNode(val)