# Definition for a  binary tree node
# class TreeNode:
#    def __init__(self, x):
#        self.val = x
#        self.left = None
#        self.right = None

class Solution:
    # @param root: root node of tree
    # @return an integer
    def isSymmetric(self, root):
        return self.executor(root, root)
    
    def executor(self, subtree1, subtree2):
        """Symmetric means root.right == root.left and 
           every right and left sub-tree are symmetric."""
        # @param subtree1 : root node of subtree(lefthand side)
        # @param subtree2 : root node of subtree(righthand side)
        # @return an integer
        if not (subtree1 or subtree2): 
            return 1
        elif (subtree1 and subtree2) and subtree1.val == subtree2.val:
            return (self.executor(subtree1.left, subtree2.right) +
                    self.executor(subtree1.right, subtree2.left)) // 2
        else: 
            return 0
        return 1
