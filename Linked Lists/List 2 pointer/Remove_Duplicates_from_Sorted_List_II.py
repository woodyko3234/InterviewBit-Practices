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
	    dupBool = False
	    output = ListNode(curr.val) 
	    head = output #not correct, need to push to the next
	    if not curr.next: return head
	    while curr:
	        if curr.next:
	            if curr.next.val == curr.val:
	                dupBool = True
	            elif dupBool == True:
	                dupBool = False
	            else:
	                output.next = ListNode(curr.val)
	                output = output.next
	        else:
	            if curr.val == output.val or dupBool == True: pass
	            else: output.next = ListNode(curr.val)
	        curr = curr.next
	    return head.next #the very next node to head is the truely heading node
