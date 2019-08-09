# Definition for singly-linked list.
# class ListNode:
#	def __init__(self, x):
#		self.val = x
#		self.next = None

class Solution:
	# @param A : head node of linked list
	# @param B : integer
	# @return the head node in the linked list
	def reverseList(self, A, B):
	    if B <= 1: return A
	    curr, i, temp = A, 0, None
	    head = ListNode(0)
	    head.next = A
	    link_head = head
	    while curr:
	        i += 1
	        if i == 1:
	            temp_end = curr
	        temp_head = curr
	        curr = curr.next
	        temp_head.next = temp
	        temp = temp_head
	        if i == B:
	            i = 0
	            link_head.next = temp_head
	            temp = None
	            temp_end.next = curr
	            link_head = temp_end
        return head.next
