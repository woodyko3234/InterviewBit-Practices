# Definition for singly-linked list.
# class ListNode:
#	def __init__(self, x):
#		self.val = x
#		self.next = None

class Solution:
	# @param A : head node of linked list
	# @return the head node in the linked list
	def deleteDuplicates(self, A):
        curr = A
	    removeDup = ListNode(curr.val)
	    head = removeDup
	    while curr:
	        if curr.val == removeDup.val: pass
	        else:
	            removeDup.next = ListNode(curr.val)
	            removeDup = removeDup.next
	        curr = curr.next
	    return head
