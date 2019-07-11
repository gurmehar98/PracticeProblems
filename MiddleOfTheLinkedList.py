class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def middleNode(self, head):
        slow = fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        return slow

if __name__ == "__main__":
    myList = ListNode(1)
    myList.next = ListNode(2)
    myList.next.next = ListNode(3)
    myList.next.next.next = ListNode(4)
    myList.next.next.next.next = ListNode(5)
    s = Solution()
    print(s.middleNode(myList))