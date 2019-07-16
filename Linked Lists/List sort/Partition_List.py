# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

'''
Given 1->4->3->2->5->2 and x = 3,
return 1->2->2->4->3->5.
why not 122345?!
bcz "all nodes less than x come before nodes greater than or equal to x."
items greater or equal to x should follow the default order.
e.g.
B = 3
A = 1, A.next = 3 => pass => A = A.next
A.next = 3, A.next.next = 2 => switch => A.next = 2 and A.next.next = 3
'''

class Solution:
    def get_node(self, head):
        """
        returns a tuple(A, B)
        A = first node of list
        B = rest of the list
        """
        
        # if list is None
        if head is None:
            return (None, None)
        
        else:
            rest = head.next
            node = head
            node.next = None
            head = rest
            return (node, head)
    
    # @param A : head node of linked list
    # @param B : integer
    # @return the head node in the linked list
    def partition(self, A, B):
        head = A
        rest = A
        x = B
        
        rednode = ListNode('red')
        bluenode = ListNode('blue')
        
        left = rednode
        right = bluenode
        
        while True:
            node, rest = self.get_node(rest)
            if node is None:
                break
            
            if node.val < x:
                left.next = node
                left = node
            else:
                right.next = node
                right = node
        
        left.next = bluenode.next
        head = rednode.next
        return head
        
