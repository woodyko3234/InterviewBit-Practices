# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    # @param A : head node of linked list
    # @param B : integer
    # @return the head node in the linked list
    def reverseList(self, A, B):
        if B == 1: return A
        cur = A
        output = []
        times = 0
        while cur != None:
            groups = [None]*(B+1)
            for i in range(B):
                after = cur.next
                groups[i] = cur
                groups[i].next = groups[i-1]
                cur = after
            output.append(groups)
            times += 1
        for i in range(times-1):
            output[i][0].next = output[i+1][B-1]
        return output[0][B-1]
            
