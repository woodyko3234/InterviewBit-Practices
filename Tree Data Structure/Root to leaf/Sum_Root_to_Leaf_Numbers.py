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
        pathlists = self.paths(root)
        sumup = 0
        for p in pathlists:
            sumup += (int(p) % 1003)
        return sumup % 1003
        
    def paths(self, root):
        self.path = []
        self.recursive(root, "")
        return self.path
        
    def recursive(self, node, string = ""):
        if node == None: return
        elif node.left == None and node.right == None:
            self.path.append(string + str(node.val))
            return 
        return (self.recursive(node.left, string + str(node.val)) or 
                self.recursive(node.right, string + str(node.val)))
