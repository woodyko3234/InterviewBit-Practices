# Definition for a  binary tree node
# class TreeNode:
#	def __init__(self, x):
#		self.val = x
#		self.left = None
#		self.right = None

class Solution:
	# @param inorderArr : list of integers
	# @param postorderArr : list of integers
	# @return the root node in the tree
	def buildTree(self, inorderArr, postorderArr):
	    '''
	    in-order-traversal: print subtree by subtree
        which is, [subtree.left, subtree, subtree.right]
        e.g. input: 1 2 3 4 5 6 7
        output: 4 2 5 1 6 3 7
        
        postorder: bottom-up, left to right appending method
        go down to the leaf layer first, and then append nodes 
        from left to right, leaf to root, stack by stack
        e.g. full binary tree 1 2 3 4 5 6 7
        => 4 5 2 6 7 3 1
	    '''
	    #rootnode = postorderArr[-1]
	    if not postorderArr: return None
        root = TreeNode(postorderArr[-1])
        rootIdx = self.findRoot(inorderArr, postorderArr)
        #right subtree includes inorderArr[i+1:]
        #left subtree contains inorderArr[:i]
        rightInorder = inorderArr[rootIdx+1:]
        leftInorder = inorderArr[:rootIdx]
        leftn = len(leftInorder)
        rightn = len(rightInorder)
        #the lengths of subtrees in each array would be the same
        leftPostorder = postorderArr[:leftn]
        rightPostorder = postorderArr[leftn:leftn+rightn]
        
        root.left = self.buildTree(leftInorder, leftPostorder)
        root.right = self.buildTree(rightInorder, rightPostorder)
        return root
    
    def findRoot(self, inorderArr, postorderArr):
        for i in range(len(inorderArr)):
            if inorderArr[i] == postorderArr[-1]:
                return i
