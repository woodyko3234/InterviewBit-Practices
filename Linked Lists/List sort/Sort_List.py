# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    # @param A : head node of linked list
    # @return the head node in the linked list
    def sortList(self, A):
        nodes = []
        while A:
            nodes.append(A)
            A = A.next
        nodes.sort(key=lambda x: x.val)
        head = ListNode('dummy')
        result = head

        for node in nodes:
            head.next = node
            head = head.next

        head.next = None
        return result.next
        



'''
A = 5->4->2->1
head = LN(5):
cur = LN(5), nextnd = LN(4), next2 = LN(2)
1. 
nextnd.next = cur
cur.next = next2
4->5->2->1
nextnd = next2, next2 = next2.next
cur = LN(5), nextnd = LN(2), next2 = LN(1)
2.
nextnd.next = cur
cur.next = next2
4->2->5->1
nextnd = next2, next2 = next2.next
cur = LN(5), nextnd = LN(1), next2 = None
3.
nextnd.next = cur
cur.next = next2
4->2->1->5
if next2 == None: back and go again

4.
cur = LN(4), nextnd = LN(2), next2 = LN(1)
2->4->1->5
5.
2->1->4->5

6.
1->2->4->5
'''
