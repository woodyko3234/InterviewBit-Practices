# Definition for a  binary tree node
# class TreeNode:
#    def __init__(self, x):
#        self.val = x
#        self.left = None
#        self.right = None

class Solution:
    # @param root : root node of tree
    # @return a list of integers
    # Using recursion is not allowed
    def inorderTraversal(self, root):
        '''
        in-order-traversal: print subtree by subtree
        which is, [subtree.left, subtree, subtree.right]
        e.g. input: 1 2 3 4 5 6 7
        output: 4 2 5 1 6 3 7
        '''
        output = []
        if not root: return output
        else:
            temp = [root]
        while temp:
            curr = temp.pop()
            if not (curr.left or curr.right):
                output.append(curr.val)
            else:
                if curr.right:
                    temp.append(curr.right)
                temp.append(TreeNode(curr.val))
                if curr.left:
                    temp.append(curr.left)
        return output
