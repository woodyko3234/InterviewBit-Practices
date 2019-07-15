# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    # @param A : head node of linked list
    # @return the head node in the linked list
    def reorderList(self, A):
        if A == None: return None
        cur = A.next
        vallist = []
        while cur:
            vallist.append(cur.val)
            cur = cur.next
        
        n = len(vallist)
        m = len(vallist)
        head = ListNode(A.val)
        cur = head
        i = 0
        while n >= 2:
            cur.next = ListNode(vallist[(m-1)-i])
            cur = cur.next
            cur.next = ListNode(vallist[i])
            cur = cur.next
            n -= 2
            i += 1
        if n == 1:
            cur.next = ListNode(vallist[i])
        return head
            
