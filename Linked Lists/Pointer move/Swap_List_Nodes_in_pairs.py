# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    # @param A : head node of linked list
    # @return the head node in the linked list
    def swapPairs(self, A):
        if A.next:
            begin = A.next
        else:
            begin = A
        first = A
        second = A.next
        while first and second:
            nextnd = second.next
            first, second = second, first
            first.next = second
            if nextnd and nextnd.next: #not None 
                second.next = nextnd.next
            else:
                second.next = nextnd
                break
            first = nextnd
            second = nextnd.next
        return begin
