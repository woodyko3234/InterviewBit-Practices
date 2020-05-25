# Definition for a  binary tree node
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    # @param root : root node of tree
    # @return the root node in the tree
    def flatten(self, root):
        """
        Given a tree (root node)
        return a tree like a linked list, with pre-order traversal method
        """
        if not root: return root
        traversal = self.preorderTraversal(root)
        fT = TreeNode(root.val)
        if len(traversal) < 2: return fT
        curr = fT
        for i in traversal[1:]:
            curr.right = TreeNode(i)
            curr = curr.right
        return fT

        
    def preorderTraversal(self, root):
        """
        preorder: top-down, left to right appending method
        go down to the leaf layer from root, append nodes 
        from left to right, root to leaf, stack by stack
        e.g. full binary tree 1 2 3 4 5 6 7
        => 1 2 4 5 3 6 7
        """
        output = []
        if not root: return output
        else:
            temp = [root]
        while temp:
            curr = temp.pop()
            output.append(curr.val)
            if curr.right:
                temp.append(curr.right)
            if curr.left:
                temp.append(curr.left)
        return output
