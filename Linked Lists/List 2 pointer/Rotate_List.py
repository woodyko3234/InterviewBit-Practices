# Definition for singly-linked list.
# class ListNode:
#    def __init__(self, x):
#        self.val = x
#        self.next = None

class Solution:
    # @param A : head node of linked list
    # @param B : integer
    # @return the head node in the linked list
    def rotateRight(self, A, B):
        n, curr = 0, A
        while curr:
            n += 1
            curr = curr.next
        if n == 0 or B % n == 0: return A
        rotIdx = n - (B % n)
        i, curL = 1, A
        lh = curL
        while curL:
            if i != rotIdx:
                i += 1
            else:
                curR = curL.next
                curL.next = None
            curL = curL.next
        rh = curR
        while curR:
            if curR.next != None:
                curR = curR.next
            else: 
                curR.next = lh
                break
        return rh
