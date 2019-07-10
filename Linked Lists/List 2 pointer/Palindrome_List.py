# Definition for singly-linked list.
# class ListNode:
#    def __init__(self, x):
#        self.val = x
#        self.next = None

class Solution:
    # @param A : head node of linked list
    # @return an integer
    def lPalin(self, A):
        n = 0
        curr = A
        while curr:
            n += 1
            curr = curr.next
        curr = A
        revll = None
        for i in range(n//2):
            nextn = curr.next
            curr.next = revll
            revll = curr
            curr = nextn
        if n % 2 == 1:
            curr = curr.next
        for i in range(n//2):
            if curr.val != revll.val: return 0
            curr = curr.next
            revll = revll.next
        return 1
