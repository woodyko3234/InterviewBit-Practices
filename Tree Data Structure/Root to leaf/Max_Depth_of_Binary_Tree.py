# Definition for a  binary tree node
# class TreeNode:
#    def __init__(self, x):
#        self.val = x
#        self.left = None
#        self.right = None

class Solution:
    # @param root : root node of tree
    # @return an integer
    def maxDepth(self, root):
        self.maxD = 0
        self.recursive(root, 0)
        return self.maxD
        
        
    def recursive(self, node, height = 0):
        if node == None: 
            if height > self.maxD:
                self.maxD = height 
            return
        return (self.recursive(node.left, height + 1) or 
                self.recursive(node.right, height + 1))
