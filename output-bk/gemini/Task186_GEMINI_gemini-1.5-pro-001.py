import heapq

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def mergeKLists(self, lists):
        minHeap = []
        for i, head in enumerate(lists):
            if head:
                heapq.heappush(minHeap, (head.val, i, head))
        dummy = ListNode(0)
        tail = dummy
        while minHeap:
            _, i, curr = heapq.heappop(minHeap)
            tail.next = curr
            tail = tail.next
            if curr.next:
                heapq.heappush(minHeap, (curr.next.val, i, curr.next))
        return dummy.next