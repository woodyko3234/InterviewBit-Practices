# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    # @param A : head node of linked list
    # @return the first node in the cycle in the linked list
    def detectCycle(self, A):
        twox, onex = A, A
        while twox or onex:
            try:
                twox = twox.next
                twox = twox.next
            except:
                return None
            onex = onex.next
            if twox == onex: break
        curr = A
        while curr.next:
            prev = curr
            curr = curr.next
            prev.next = None
        return curr
