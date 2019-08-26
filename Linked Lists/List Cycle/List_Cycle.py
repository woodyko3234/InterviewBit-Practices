# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

from collections import defaultdict
class Solution:
    # @param A : head node of linked list
    # @return the first node in the cycle in the linked list
    def detectCycle(self, A):
        checklist = defaultdict(int)
        cur = A
        second = A
        while cur:
            checklist[cur] += 1
            if checklist[cur] == 2:
                while second:
                    if second == cur:
                        return second
                    second = second.next
            cur = cur.next
        return None

'''
A = 1->2->3->4->3->4........
output = LN(3)
'''
