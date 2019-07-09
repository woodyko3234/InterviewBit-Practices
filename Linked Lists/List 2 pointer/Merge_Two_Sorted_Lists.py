# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    # @param A : head node of linked list
    # @param B : head node of linked list
    # @return the head node in the linked list
    def mergeTwoLists(self, A, B):
        
        curA, curB = A, B
        
        output = [None, None]
        
        while curA and curB:
            nextA, nextB = curA.next, curB.next
            if curA.val > curB.val:
                if output[0] == None:
                    output[0] = curB
                else:
                    output[1].next = curB
                output[1] = curB
                curB = nextB
            else:
                if output[0] == None:
                    output[0] = curA
                else:
                    output[1].next = curA
                output[1] = curA
                curA = nextA
        if curA:
            output[1].next = curA
        else:
            output[1].next = curB
        return output[0]
