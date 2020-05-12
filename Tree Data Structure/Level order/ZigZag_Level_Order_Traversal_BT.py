# Definition for a  binary tree node
# class TreeNode:
#    def __init__(self, x):
#        self.val = x
#        self.left = None
#        self.right = None

class Solution:
    # @param root : root node of tree
    # @return a list of list of integers
    def zigzagLevelOrder(self, root):
        output = self.traversal(root, [[]], 0)
        n = len(output)
        for i in range(n):
            if i % 2 == 1:
                output[i] = output[i][::-1]
        return output
    
    def traversal(self, node, output = [[]], level = 0):
        if level + 1 > len(output):
            output.append([])
        if node:
            output[level].append(node.val)
        if node.left:
            self.traversal(node.left, output, level+1)
        if node.right:
            self.traversal(node.right, output, level+1)
        return output
