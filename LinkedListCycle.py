class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def hasCycle(self, head):
        try:
            slow, fast = head, head.next
            while slow != fast: slow, fast = slow.next, fast.next.next
            return True
        except: return False  