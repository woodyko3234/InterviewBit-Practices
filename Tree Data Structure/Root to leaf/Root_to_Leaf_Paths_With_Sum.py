# Definition for a  binary tree node
# class TreeNode:
#    def __init__(self, x):
#        self.val = x
#        self.left = None
#        self.right = None

class Solution:
    # @param root : root node of tree
    # @param T : Targeted integer
    # @return a list of list of integers
    def pathSum(self, root, T):
        self.path = []
        self.recursive(root, T, [])
        return self.path
        
    def recursive(self, node, R, lst = []):
        if node == None: return
        elif node.left == None and node.right == None:
            if R - node.val == 0: 
                self.path.append(lst + [node.val])
            return 
        return (self.recursive(node.left, R - node.val, lst + [node.val]) or 
                self.recursive(node.right, R - node.val, lst + [node.val]))
