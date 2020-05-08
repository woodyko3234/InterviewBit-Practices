# Definition for a  binary tree node
# class TreeNode:
#    def __init__(self, x):
#        self.val = x
#        self.left = None
#        self.right = None

class Solution:
    # @param A : list of integers
    # @return the root node in the tree
    def buildTree(self, A):
        """
        Max Cartesian Tree:
        1. The tree obeys in the max heap property – 
        each node is greater than its children.
        2. An inorder traversal of the nodes yields the values 
        in the same order in which they appear in the initial sequence.
        
        Note:
        1. Cartesian Tree is not a height-balanced tree.
        2. Cartesian tree of a sequence of distinct numbers is always unique.
        """
        #find the root
        if not A: return A
        root, n = TreeNode(A[-1]), len(A)
        if n == 1: return root
        subtree_R, subtree_L = root.right, root.left
        for i in range(n-2, -1, -1):
            if A[i] > root.val:
                #update right subtree
                subtree_R = root
                root = TreeNode(A[i])
                root.right = subtree_R
                #checked, correct
            else:
                #update left subtree
                #more difficult, solution is not complete binary trees
                subtree_L = self.subtreeUpdate(A[i],root.left)
                root.left = subtree_L
        #O(n^2) solution
        return root
                
    def subtreeUpdate(self, val, subtree_L):
        if not subtree_L: 
            subtree_L = TreeNode(val)
            return subtree_L
        elif val > subtree_L.val:
            subroot = subtree_L
            subtree_L = TreeNode(val)
            subtree_L.left = subroot
            return subtree_L
        elif not subtree_L.left:
            subtree_L.left = TreeNode(val)
            return subtree_L
        subroot, curr = subtree_L, subtree_L.left
        while curr.left:
            if val > curr.val:
                subroot.left = TreeNode(val)
                subroot.left.left = curr
                return subtree_L
            else:
                curr = curr.left
                subroot = subroot.left
        curr.left = TreeNode(val)
        return subtree_L
