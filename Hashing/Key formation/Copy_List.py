# Definition for singly-linked list with a random pointer.
# class RandomListNode:
#     def __init__(self, x):
#         self.label = x
#         self.next = None
#         self.random = None

class Solution:
    # @param head, a RandomListNode
    # @return a RandomListNode
    def copyRandomList(self, head):
        cache = {}
        curr = head
        while(curr):
            if curr not in cache:
                cache[curr] = RandomListNode(curr.label)
            
            if curr.next:
                if curr.next not in cache:
                    cache[curr.next] = RandomListNode(curr.next.label)
                cache[curr].next = cache[curr.next]
           
            if curr.random:
                if curr.random not in cache:
                    cache[curr.random] = RandomListNode(curr.random.label)
                cache[curr].random = cache[curr.random]
           
            curr = curr.next
        return cache[head]
