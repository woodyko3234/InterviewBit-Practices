# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    # @param A : head node of linked list
    # @param B : integer
    # @return the head node in the linked list
    def rotateRight(self, A, B):
        #compute length first
        cur = A
        n = 0
        while cur:
            n += 1
            cur = cur.next
        
        if B % n == 0: #no rotation
            return A
        B = B % n    
        #reset
        cur = A
        head = A
        while cur:
            nextnd = cur.next
            if (n-1) == B:
                prev = cur
                cur = nextnd
                prev.next = None
                output = nextnd
            else:
                if nextnd != None:
                    cur = nextnd
                else:
                    cur.next = head
                    return output
            n -= 1    
'''
A = 1->2->3->4->5->None
B = 5, output = A;
B = 2, output = 4->5->1->2->3->None

so, prev should be recognized before cur is approached, and prev.next should be modified as None
and when (cur.next = None) is hit, cur.next should be linked to the head node

'''
