# Definition for singly-linked list.
# class ListNode:
#	def __init__(self, x):
#		self.val = x
#		self.next = None

class Solution:
	# @param A : head node of linked list
	# @param B : head node of linked list
	# @return the head node in the linked list
	def mergeTwoLists(self, A, B):
	    if not (A or B): return None
	    elif not A: return B
	    elif not B: return A
	    currA, currB = A, B
	    merged = None
	    while currA and currB:
	        if currA.val > currB.val:
	            if merged:
	                merged.next = ListNode(currB.val)
	                merged = merged.next
	            else:
	                merged = ListNode(currB.val)
	                head = merged
	            currB = currB.next
	        else:
	            if merged:
                        merged.next = ListNode(currA.val)
                        merged = merged.next
                    else:
                        merged = ListNode(currA.val)
                        head = merged
                    currA = currA.next
	    if currA: merged.next = currA
	    else: merged.next = currB
	    return head
