# Definition for a  binary tree node
# class TreeNode:
#    def __init__(self, x):
#        self.val = x
#        self.left = None
#        self.right = None

class Solution:
    # @param root: root node of tree
    # @return an integer
    def minDepth(self, root):
        self.minD = float("inf")
        self.recursive(root, 1)
        return self.minD
        
    def recursive(self, node, height = 1):
        #leaf definition
        if not (node.left or node.right): 
            if height < self.minD:
                self.minD = height 
            return
        if node.left:
            self.recursive(node.left, height + 1)
        if node.right:
            self.recursive(node.right, height + 1)
        return
