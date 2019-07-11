class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def removeElements(self, head, val):
        curr = head
        while curr:
            while curr.next and curr.val == val:
                curr.next = curr.next.next
            curr = curr.next
        return head