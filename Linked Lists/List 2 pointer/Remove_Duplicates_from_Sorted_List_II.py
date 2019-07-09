# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    # @param A : head node of linked list
    # @return the head node in the linked list
    def deleteDuplicates(self, A):
        newll = None
        head = None
        cur = A
        notDuplicates = True
        
        while cur:
            nextnd = cur.next
            if nextnd != None and nextnd.val == cur.val:
                notDuplicates = False
            elif nextnd != None and nextnd.val != cur.val:    
                if notDuplicates and newll == None:
                    newll = ListNode(cur.val)
                    head = newll
                elif notDuplicates:
                    newll.next = ListNode(cur.val)
                else:
                    notDuplicates = True
            #nextnd == None, checking the last node
            elif notDuplicates and newll == None: 
                newll = ListNode(cur.val)
                head = newll
            elif notDuplicates:
                newll.next = ListNode(cur.val)
                
            cur = nextnd
            if newll and newll.next:
                newll = newll.next
        
        return head
