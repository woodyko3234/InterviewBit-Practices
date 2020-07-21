# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    # @param lst: list of linked list
    # @return the head node in the linked list
    def mergeKLists(self, lst):
        tempMerger = []
        while len(lst) + len(tempMerger) > 1:
            while len(lst) > 1:
                linklst1, linklst2 = lst.pop(), lst.pop()
                tempMerger.append(self.merger(linklst1, linklst2))
            while len(tempMerger) > 1:
                linklst1, linklst2 = tempMerger.pop(), tempMerger.pop()
                lst.append(self.merger(linklst1, linklst2))
            if lst:
                tempMerger.append(lst.pop())
        if lst:
            return lst.pop()
        return tempMerger.pop()
    
    def merger(self, linklst1, linklst2):
        curr1, curr2 = linklst1, linklst2
        if curr1.val > curr2.val:
            root = curr2
            curr2 = curr2.next
        else:
            root = curr1
            curr1 = curr1.next
        
        temp = root
        while curr1 and curr2:
            if curr1.val > curr2.val:
                temp.next = curr2
                curr2 = curr2.next
            else:
                temp.next = curr1
                curr1 = curr1.next
            temp = temp.next
        if curr1:
            temp.next = curr1
        else:
            temp.next = curr2
        return root
