# Definition for singly-linked list.
# class ListNode:
#    def __init__(self, x):
#        self.val = x
#        self.next = None

class Solution:
    # @param A : head node of linked list
    # @param B : head node of linked list
    # @return the head node in the linked list
    def addRest(self, restLL, addOne):
        head = ListNode(0)
        curr = head
        while restLL:
            currCom = restLL.val
            if addOne:
                currCom += 1
                addOne = False
            if currCom > 9:
                addOne = True
                currCom -= 10
            curr.next = ListNode(currCom)
            #Push
            curr = curr.next
            restLL = restLL.next
        if addOne:
            curr.next = ListNode(1)
            addOne = False
        return head.next
        
    def addTwoNumbers(self, A, B):
        """
        combine A & B, without convert the linked lists into integers
        """
        combinedLL = ListNode(0)
        curr = combinedLL
        currA, currB = A, B
        addOne = False
        while currA and currB:
            currCom = currA.val + currB.val
            if addOne:
                currCom += 1
                addOne = False
            if currCom > 9:
                addOne = True
                currCom -= 10
            curr.next = ListNode(currCom)
            #Push
            curr = curr.next
            currA = currA.next
            currB = currB.next
        if currA:
            curr.next = self.addRest(currA, addOne)
        elif currB:
            curr.next = self.addRest(currB, addOne)
        elif addOne:
            curr.next = ListNode(1)
            addOne = False
        return combinedLL.next
