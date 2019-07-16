# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    # @param A : head node of linked list
    # @return the head node in the linked list
    def insertionSortList(self, A):
        cur = A
        values = []
        while cur:
            values.append(cur.val)
            cur = cur.next
        
        values.sort()
        
        output = looper = ListNode(values[0])
        for i in values[1:]:
            looper.next = ListNode(i) or None
            looper = looper.next
        return output
