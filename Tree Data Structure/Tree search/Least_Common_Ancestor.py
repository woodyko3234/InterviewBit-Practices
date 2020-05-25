# Definition for a  binary tree node
# class TreeNode:
#    def __init__(self, x):
#        self.val = x
#        self.left = None
#        self.right = None

class Solution:
    # @param root : root node of tree
    # @param tA : targeted integer A
    # @param tB : targeted integer B
    # @return an integer
    def lca(self, root, tA, tB):
        if not root: return -1
        ancestorsA = self.searchChild(root, tA, [])
        ancestorsB = self.searchChild(root, tB, [])
        if ancestorsA == False or ancestorsB == False:
            return -1
        ancestorsA, ancestorsB = ancestorsA[::-1], ancestorsB[::-1]
        
        while len(ancestorsA) > 0 and len(ancestorsB) > 0:
            #find the first different ancestors of A and B
            currA, currB = ancestorsA.pop(), ancestorsB.pop()
            if currA == currB: 
                LCA = currA
                continue
            else: break
        return LCA
        
    def searchChild(self, node, tV, ancestors = []):
        if node == None: return False
        elif node.val == tV:
            return ancestors + [node.val]
        else:
            return (self.searchChild(node.left, tV, ancestors + [node.val]) or 
                    self.searchChild(node.right, tV, ancestors + [node.val]))
