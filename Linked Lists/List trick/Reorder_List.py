# Definition for singly-linked list.
# class ListNode:
#	def __init__(self, x):
#		self.val = x
#		self.next = None

class Solution:
	# @param A : head node of linked list
	# @return the head node in the linked list
	def reorderList(self, A):
	    leftLL, rightLL = self.divideList(A)
	    if not rightLL: return leftLL
	    rightLL = self.reverseList(rightLL)
	    head = ListNode(0)
	    curr = head
	    leftN, rightN = leftLL, rightLL
	    while rightN:
	        curr.next = leftN
	        curr, leftN = curr.next, leftN.next
	        curr.next = rightN
	        curr, rightN = curr.next, rightN.next
        curr.next = leftN
        return head.next
	    
	    
    def divideList(self, A):
        curr, left, mid = A, A, A
        while curr:
            curr = curr.next
            if curr:
                curr = curr.next
                mid = mid.next
        right = mid.next
        mid.next = None
        return left, right
        
    def reverseList(self, right):
        if not right.next: return right
        head = ListNode(0)
        curr, temp = right.next, ListNode(right.val)
        while curr:
            head.next = curr
            curr = curr.next
            head.next.next = temp
            temp = head.next
        return head.next
