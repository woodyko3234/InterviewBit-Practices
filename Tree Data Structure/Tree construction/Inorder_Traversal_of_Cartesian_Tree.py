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
        start, end = 0, len(A) - 1
        return self.builder(A, start, end)
        
    def builder(self, A, start, end): 
        if start > end: 
            return None
        #find the index of the maximum in input array
        i = self.findMax(A, start, end)
        
        # Pick the maximum value and make it root  
        root = TreeNode(A[i])
        
        # If this is the only element in  
        # inorder[start..end], then return it  
        if start == end:
            return root
            
        # Using index in Inorder traversal,  
        # construct left and right subtress
        root.left = self.builder(A, start, i - 1)
        root.right = self.builder(A, i + 1, end)
        return root 

    def findMax(self, arr, start, end): 
        i, Max = 0, arr[start] 
        maxind = start 
        for i in range(start + 1, end + 1): 
            if arr[i] > Max: 
                Max = arr[i]
                maxind = i
        return maxind
  
