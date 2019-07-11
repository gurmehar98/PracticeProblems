class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def reverseList(self, head):
        prev = None
        curr = head
        while head:
            curr = head
            head = head.next
            curr.next = prev
            prev = curr
        return curr

if __name__ == "__main__":
    myList = ListNode(1)
    myList.next = ListNode(2)
    myList.next.next = ListNode(3)
    myList.next.next.next = ListNode(4)
    myList.next.next.next.next = ListNode(5)
    s = Solution()
    print(s.reverseList(myList))