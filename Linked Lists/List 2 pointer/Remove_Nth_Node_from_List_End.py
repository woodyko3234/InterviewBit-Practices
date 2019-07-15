# Definition for singly-linked list.
# class ListNode:
#    def __init__(self, x):
#        self.val = x
#        self.next = None

class Solution:
    # @param A : head node of linked list
    # @param B : integer
    # @return the head node in the linked list
    def removeNthFromEnd(self, A, B):
        n, curr = 0, A
        while curr:
            n += 1
            curr = curr.next
        if n <= B: return A.next
        toDrop, i, curr = n - B, 1, A
        head = curr
        while curr:
            if i != toDrop:
                i += 1
            elif B == 1 and i == n - 1:
                curr.next = None
            else:
                curr.next = curr.next.next
                break
            curr = curr.next
        return head
