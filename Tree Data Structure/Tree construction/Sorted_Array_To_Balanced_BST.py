# Definition for a  binary tree node
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    # @param arr : tuple of integers
    # @return the root node in the tree
    def sortedArrayToBST(self, arr):
        """
        divide the array into two: left and right
        left: smaller than the root node
        right: bigger than the root node
        with recursion, the tree would be balanced automatically.
        """
        n = len(arr)
        start, end = 0, n
        return self.builder(arr, start, end)
    
    def builder(self, arr, start, end):
        if start >= end: return
        mid = (start + end)//2
        root = TreeNode(arr[mid])
        root.left = self.builder(arr, start, mid)
        root.right = self.builder(arr, mid+1, end)
        return root
