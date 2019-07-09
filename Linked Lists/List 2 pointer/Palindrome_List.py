# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None


'''
build another linked list backwards
'''
class Solution:
    # @param A : head node of linked list
    # @return an integer
    def linkedListBack(self, A):
        cur = ListNode(A.val)
        prev = None
        fur = A
        while fur != None:
            cur, fur  = ListNode(fur.val), fur.next
            cur.next = prev
            prev = cur

        return cur
    
    def lPalin(self, A):
        cur = self.linkedListBack(A)
        while A != None and cur != None:
            if A.val == cur.val:
                A = A.next
                cur = cur.next
            else:
                return 0
        return 1
