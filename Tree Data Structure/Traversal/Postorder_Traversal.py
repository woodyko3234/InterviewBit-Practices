# Definition for a  binary tree node
# class TreeNode:
#    def __init__(self, x):
#        self.val = x
#        self.left = None
#        self.right = None

class Solution:
    # @param A : root node of tree
    # @return a list of integers
    def postorderTraversal(self, A):
        if not A:
            return []
        stack1 = [A]
        stack2 = []
        
        while len(stack1) > 0:
            current = stack1.pop()
            stack2.append(current.val)
            
            if current.left is not None:
                stack1.append(current.left)
            if current.right is not None:
                stack1.append(current.right)
        
        return stack2[::-1]
