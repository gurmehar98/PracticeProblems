import heapq

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def mergeKLists(self, lists):
        mergeHeap = [(head.val, i, head) for i, head in enumerate(lists) if head]
        heapq.heapify(mergeHeap)
        temp = curr = ListNode(None)
        while mergeHeap:
            _, i, node = mergeHeap[0]
            if node.next != None: heapq.heapreplace(mergeHeap, (node.next.val, i, node.next))
            else: heapq.heappop(mergeHeap)
            curr.next = node
            curr = curr.next
        return temp.next

if __name__ == "__main__":
    l1 = ListNode(1)
    l1.next = ListNode(4)
    l1.next.next = ListNode(5)
    l2 = ListNode(1)
    l2.next = ListNode(3)
    l2.next.next = ListNode(4)
    l3 = ListNode(2)
    l3.next = ListNode(6)
    lists = [l1, l2, l3]
    s = Solution()
    print(s.mergeKLists(lists))