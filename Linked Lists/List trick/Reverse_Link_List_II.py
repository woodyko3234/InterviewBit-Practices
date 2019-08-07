# Definition for singly-linked list.
# class ListNode:
#	def __init__(self, x):
#		self.val = x
#		self.next = None

class Solution:
	# @param A : head node of linked list
	# @param m : integer
	# @param n : integer
	# @return the head node in the linked list
	def reverseBetween(self, A, m, n):
	    if m == n: return A
	    i = 0
	    head = ListNode(0)
	    head.next = A
	    curr = head
	    while curr:
	        if i == m-1:
	            cur_end = curr
	        elif i == m:
	            start = curr
	            curr = curr.next
	            i += 1
	            start.next = None
	            temp = start
	            continue
	        elif n >= i > m:
	            cur_end.next = curr
	            curr = curr.next
	            cur_end.next.next = temp
	            temp = cur_end.next
	            if i == n:
	                start.next = curr
	                break
                i += 1
	            continue
	        curr = curr.next
	        i += 1
        return head.next
