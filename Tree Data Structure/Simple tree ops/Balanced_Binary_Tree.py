# Definition for a  binary tree node
# class TreeNode:
#    def __init__(self, x):
#        self.val = x
#        self.left = None
#        self.right = None

class Solution:
    # @param A : root node of tree
    # @return an integer
    def isBalanced(self, A):
        if A is None or (A.left is None and A.right is None): 
            return 1
        queue = [A]
        while len(queue) > 0:
            T = queue.pop()
            if T.left: 
                queue.append(T.left)
                if not T.right and (T.left.left or T.left.right):
                    return 0
            if T.right:
                queue.append(T.right)
                if not T.left and (T.right.left or T.right.right):
                    return 0
        return 1
