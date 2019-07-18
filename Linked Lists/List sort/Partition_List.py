# Definition for singly-linked list.
# class ListNode:
#	def __init__(self, x):
#		self.val = x
#		self.next = None

class Solution:
	# @param A : head node of linked list
	# @param B : integer
	# @return the head node in the linked list
	def partition(self, A, B):
	    if A == None: return A
	    leftll, rightll, curr = None, None, A
	    while curr:
	        if curr.val < B:
	            if leftll == None: 
	                leftll = ListNode(curr.val)
	                fnl = leftll #first node of leftll
	            else: 
	                leftll.next = ListNode(curr.val)
	                leftll = leftll.next
	        else:
	            if rightll == None:
	                rightll = ListNode(curr.val)
	                fnr = rightll #first node of rightll
	            else:
	                rightll.next = ListNode(curr.val)
	                rightll = rightll.next
	        curr = curr.next
	    if leftll: 
	        if rightll: leftll.next = fnr
	        return fnl
	    else: return fnr
