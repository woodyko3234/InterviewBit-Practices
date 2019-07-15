# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    # @param A : head node of linked list
    # @param m : integer
    # @param n : integer
    # @return the head node in the linked list
    def reverseBetween(self, A, m, n):
        if m == n: return A
        cur = A
        length = 0
        prev = None
        head = A
        while cur:
            length += 1
            nextnd = cur.next
            if length < m:
                prev = cur
                cur = nextnd
            else: #length >= m
                lnList = []
                for i in range(m, n+1):
                    lnList.append(cur.val)
                    cur = cur.next
                if prev == None: #m = 1
                    head = ListNode(lnList[-1])
                    prev = head
                    for i in lnList[-2::-1]:
                        prev.next = ListNode(i)
                        prev = prev.next
                    prev.next = cur
                    return head
                else:
                    for i in lnList[::-1]:
                        prev.next = ListNode(i)
                        prev = prev.next
                    prev.next = cur
                    return head

        return head
