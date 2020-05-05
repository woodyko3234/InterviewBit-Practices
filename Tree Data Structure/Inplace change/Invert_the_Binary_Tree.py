# Definition for a  binary tree node
# class TreeNode:
#    def __init__(self, x):
#        self.val = x
#        self.left = None
#        self.right = None

class Solution:
    # @param A : root node of tree
    # @return the root node in the tree
    def invertTree(self, A):
        inverseA = TreeNode(A.val)
        return self.executor(A, inverseA)
        
    def executor(self, A, inverseA):
        """
        inverseA: inversed tree A
        inverseA.left = A.right, inverseA.right = A.left
        should do it recursively
        question: how to create subtrees in the inversed tree?
        """
        if not (A.left or A.right): return inverseA
        else:
            if A.left:
                inverseA.right = TreeNode(A.left.val)
                self.executor(A.left, inverseA.right)
            else:
                inverseA.right = None
            if A.right:
                inverseA.left = TreeNode(A.right.val)
                self.executor(A.right, inverseA.left)
            else:
                inverseA.left = None
        return inverseA
