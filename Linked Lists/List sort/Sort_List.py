# Definition for singly-linked list.
# class ListNode:
#	def __init__(self, x):
#		self.val = x
#		self.next = None

class Solution:
	# @param A : head node of linked list
	# @return the head node in the linked list
	def sortList(self, A):
	    '''Merge Sort is recommended.
	       step1. break the linked list into small lists
	       step2. sort the small lists one by one
	       step3. compare and combine the small lists.'''
	    if not A.next: return A
	    mid = self.getMid(A)
        next_of_mid = mid.next
        mid.next = None
        
        left = self.sortList(A)
        right = self.sortList(next_of_mid)
        
        result = self.mergeSort(left, right)
        
        return result

        
    def getMid(self, A):
        """get the mid point with while loop"""
        if not A or not A.next: return A
        mid, curr = A, A.next
        while curr:
            curr = curr.next
            if curr:
                mid = mid.next
                curr = curr.next
        return mid
    
    def mergeSort(self, left, right):
        """apply merge sort into the separated linked lists"""
        if not left: return right
        elif not right: return left
        head = ListNode(float("-inf"))
        output = head
        while left and right:
            if left.val > right.val:
                output.next = ListNode(right.val)
                right = right.next
            else:
                output.next = ListNode(left.val)
                left = left.next
            output = output.next
        if left:
            output.next = left
        elif right:
            output.next = right
        return head.next
