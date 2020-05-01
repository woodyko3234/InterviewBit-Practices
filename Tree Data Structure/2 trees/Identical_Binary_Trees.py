# Definition for a  binary tree node
# class TreeNode:
#    def __init__(self, x):
#        self.val = x
#        self.left = None
#        self.right = None

class Solution:
    # @param root_A : root node of tree
    # @param root_B : root node of tree
    # @return an integer
    def isSameTree(self, root_A, root_B):
        if root_A == None and root_B == None:
            pass
        elif root_A == None or root_B == None: 
            #print("notsametree")
            return 0
        elif not self.isSameBranch(root_A, root_B): 
            #print("notsamebranch")
            return 0
        elif not self.isSameNode(root_A, root_B):
            #print("notsamenode")
            return 0
        else:
            if self.isSameTree(root_A.left, root_B.left) == 0 or self.isSameTree(
                root_A.right, root_B.right) == 0: return 0
        return 1
        
    def isSameNode(self, node_A, node_B):
        if node_A.val != node_B.val: return 0
        return 1
    
    def isLeaf(self, d):
        if d.left is None and d.right is None:
            return 1
        return 0
    
    def isSameBranch(self, node_A, node_B):
        if (node_A.left and not node_B.left) or (not node_A.left and node_B.left):
            return 0
        elif (node_A.right and not node_B.right) or (not node_A.right and node_B.right):
            return 0
        return 1
