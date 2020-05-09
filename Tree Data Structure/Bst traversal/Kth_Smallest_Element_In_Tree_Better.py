# Definition for a  binary tree node
# class TreeNode:
#    def __init__(self, x):
#        self.val = x
#        self.left = None
#        self.right = None

class Solution:
    # @param A : root node of tree
    # @param B : integer
    # @return an integer
    def kthsmallest(self, A, B):
        # working stack
        s = []
        
        # traverse to the left most leaf node (minimum)
        cur = A
        while cur:
            s.append(cur)
            cur = cur.left
            
        # pre-order traversal and keep count
        k = 0    
        while s:
            n = s.pop()
            k+=1
            if k == B:
                return n.val
            cur = n.right;
            while cur:
                s.append(cur)
                cur = cur.left
        return -1
