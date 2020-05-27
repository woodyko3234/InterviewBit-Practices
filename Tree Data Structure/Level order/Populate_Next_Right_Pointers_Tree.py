# Definition for a  binary tree node
# class TreeLinkNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
#         self.next = None

class Solution:
    # @param root, a tree node
    # @return nothing
    def connect(self, root):
        self.levels = [[]]
        newRoot = TreeLinkNode(root.val)
        self.traversal(root, newRoot, newRoot, level = 0)
        for l in range(len(self.levels)-1):
            self.levels[l][-1].next = self.levels[l+1][0]
        for l in range(len(self.levels)-1):
            self.levels[l][-1].next = None
        return self.levels[0][0]
        
    def traversal(self, node, newTree, root, level = 0):
        if not node: return 
        if len(self.levels) < level+1:
            self.levels.append([])
        if node.left:
            newTree.left = TreeLinkNode(node.left.val)
            self.traversal(node.left, newTree.left, root, level+1)
        if node.right:
            newTree.right = TreeLinkNode(node.right.val)
            self.traversal(node.right, newTree.right, root, level+1)
        self.levels[level].append(newTree)
        if len(self.levels[level]) > 1:
            self.levels[level][-2].next = newTree
        return 
