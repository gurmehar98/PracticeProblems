class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def deleteDuplicates(self, head):
        curr = head
        while curr:
            while curr.next and curr.next.val == curr.val:
                curr.next = curr.next.next
            curr = curr.next 
        return head

if __name__ == "__main__":
    myList = ListNode(1)
    myList.next = ListNode(1)
    myList.next.next = ListNode(2)
    s = Solution()
    print(s.deleteDuplicates(myList))