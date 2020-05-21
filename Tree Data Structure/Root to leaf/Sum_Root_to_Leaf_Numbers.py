# Definition for a  binary tree node
# class TreeNode:
#    def __init__(self, x):
#        self.val = x
#        self.left = None
#        self.right = None

class Solution:
    # @param root : root node of tree
    # @return an integer
    def sumNumbers(self, root):
        self.sumup = 0
        self.recursive(root, "")
        return self.sumup % 1003
        
    def recursive(self, node, string = ""):
        if node == None: return
        elif node.left == None and node.right == None:
            self.sumup += (int((string + str(node.val))) % 1003)
            return 
        return (self.recursive(node.left, string + str(node.val)) or 
                self.recursive(node.right, string + str(node.val)))
