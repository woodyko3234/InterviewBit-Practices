# Definition for a  binary tree node
# class TreeNode:
#    def __init__(self, x):
#        self.val = x
#        self.left = None
#        self.right = None

class Solution:
    # @param root : root node of tree
    # @param T : targeted integer
    # @return an integer
    def t2Sum(self, root, T):
        #check whether there are two nodes to sum up as T
        sortedArr = self.inorderTraversal(root)
        n = len(sortedArr)
        if n > 2 and (T > sortedArr[-1] + sortedArr[-2] or
                      T < sortedArr[0] + sortedArr[1]):
            return 0 
        idx1, idx2 = 0, n-1
        while idx1 < idx2:
            if T > (sortedArr[idx1] + sortedArr[idx2]):
                idx1 += 1
            elif T < (sortedArr[idx1] + sortedArr[idx2]):
                idx2 -= 1
            else: return 1
        return 0
        
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
