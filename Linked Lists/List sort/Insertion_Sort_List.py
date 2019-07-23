# Definition for singly-linked list.
# class ListNode:
#    def __init__(self, x):
#        self.val = x
#        self.next = None

class Solution:
    # @param A : head node of linked list
    # @return the head node in the linked list
    def insertionSortList(self, A):
        if not A: return A
        curr, sortedLL = A.next, ListNode(A.val)
        sLL_h = sortedLL
        while curr:
            prev = None
            while sortedLL:
                if sortedLL.val < curr.val:
                    prev = sortedLL
                    if sortedLL.next:
                        sortedLL = sortedLL.next
                    else:
                        sortedLL.next = ListNode(curr.val)
                        break
                elif prev:
                    prev.next = ListNode(curr.val)
                    prev.next.next = sortedLL
                    break
                else:
                    prev = ListNode(curr.val)
                    prev.next = sLL_h
                    sLL_h = prev
                    break
            sortedLL = sLL_h
            curr = curr.next
        return sLL_h
                
