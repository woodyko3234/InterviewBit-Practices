# Definition for a  binary tree node
# class TreeNode:
#    def __init__(self, x):
#        self.val = x
#        self.left = None
#        self.right = None

class Solution:
    # @param root : root node of tree
    # @param T : Targeted integer
    # @return an integer
    def hasPathSum(self, root, T):
        #has to be a valid root-to-leaf route
        #leaf: a node with no any children
        return self.recursive(root, T)
        
    def recursive(self, node, R):
        if node == None: return 0
        elif node.left == None and node.right == None:
            if R - node.val == 0: return 1
            return 0
        return (self.recursive(node.left, R - node.val) or 
                self.recursive(node.right, R - node.val))
