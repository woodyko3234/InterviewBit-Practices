# Definition for a  binary tree node
# class TreeNode:
#    def __init__(self, x):
#        self.val = x
#        self.left = None
#        self.right = None

class Solution:
    # @param preorderArr : list of integers
    # @param inorderArr : list of integers
    # @return the root node in the tree
    def buildTree(self, preorderArr, inorderArr):
        """
        preorder: top-down, left to right appending method
        go down to the leaf layer from root, append nodes 
        from left to right, root to leaf, stack by stack
        e.g. full binary tree 1 2 3 4 5 6 7
        => 1 2 4 5 3 6 7
        in-order-traversal: print subtree by subtree
        which is, [subtree.left, subtree, subtree.right]
        e.g. input: 1 2 3 4 5 6 7
        output: 4 2 5 1 6 3 7
        """
        if not preorderArr: return None
        root = TreeNode(preorderArr[0])
        rootIdx = self.findRoot(root, inorderArr)
        #divide the remaining into left and right subtrees
        leftInorder = inorderArr[:rootIdx]
        rightInorder = inorderArr[rootIdx+1:]
        #the lengths of subtrees in each array would be the same
        leftn = len(leftInorder)
        rightn = len(rightInorder)
        leftPreorder = preorderArr[1:1+leftn]
        rightPreorder = preorderArr[1+leftn:1+leftn+rightn]
        
        root.left = self.buildTree(leftPreorder, leftInorder)
        root.right = self.buildTree(rightPreorder, rightInorder)
        return root


    def findRoot(self, root, inorderArr):
        for i in range(len(inorderArr)):
            if root.val == inorderArr[i]:
                return i
