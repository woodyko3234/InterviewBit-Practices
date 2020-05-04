# Definition for a  binary tree node
# class TreeNode:
#    def __init__(self, x):
#        self.val = x
#        self.left = None
#        self.right = None

class Solution:
    # @param root : root node of tree
    # @return a list of integers
    # Using recursion is not allowed.
    def postorderTraversal(self, root):
        """
        postorder: bottom-up, left to right appending method
        go down to the leaf layer first, and then append nodes 
        from left to right, leaf to root, stack by stack
        e.g. full binary tree 1 2 3 4 5 6 7
        => 4 5 2 6 7 3 1
        """
        output = []
        if not root: return output
        else:
            temp = [root]
        while temp:
            curr = temp.pop()
            output.append(curr.val)
            if curr.left:
                temp.append(curr.left)
            if curr.right:
                temp.append(curr.right)
        return output[::-1]
        
