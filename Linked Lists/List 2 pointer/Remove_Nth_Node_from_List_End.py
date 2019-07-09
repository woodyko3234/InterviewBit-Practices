# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    # @param A : head node of linked list
    # @param B : integer
    # @return the head node in the linked list
    def removeNthFromEnd(self, A, B):
        cur = A
        n = 0
        #compute the length
        while cur:
            n += 1
            cur = cur.next
        
        if n <= B:
            A = A.next
            return A
        #reset    
        cur = A
        
        while cur:
            nextnd = cur.next
            if n != B:
                prev = cur
            else:
                prev.next = nextnd #skip cur
            cur = nextnd
            n -= 1
        return A
'''
A = 1->2->3->4->5
B = 5, output = 2->3->4->5
first while loop => n = 5
cur = LN(1)
nextnd = LN(2)
def solved the B=5
e.g. B = 2, output = 1->2->3->5
cur = LN(1)
nextnd = LN(2)
when n = 2: cur = LN(4)
'''
        
