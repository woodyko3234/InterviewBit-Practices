# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    # @param A : head node of linked list
    # @return the head node in the linked list
    def deleteDuplicates(self, A):
        output = [A, None]
        cur = A
        i = 0
        while cur:
            after = cur.next
            if output[i].val != cur.val:
                output[i+1] = cur
                output[i+1].next = None
                output[i].next = output[i+1]
                i += 1
                output = output + [None]
            cur = after
        output[0].next = output[1]
        return output[0]
