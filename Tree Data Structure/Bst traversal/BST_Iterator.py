# Definition for a  binary tree node
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class BSTIterator:
    # @param root, a binary search tree's root node
    def __init__(self, root):
        self.arr = [root]

    # @return a boolean, whether we have a next smallest number
    def hasNext(self):
        if self.arr and self.arr[0]: return True
        return False

    # @return an integer, the next smallest number
    def next(self):
        #return value with inorder traversal
        if self.arr[-1].left:
            temp = self.arr[-1].left
            while temp:
                self.arr.append(temp)
                temp = temp.left
        temp = self.arr.pop()
        if self.arr:
            self.arr[-1].left = None
        if temp.right:
            self.arr.append(temp.right)
        return temp.val
        
        

# Your BSTIterator will be called like this:
# i = BSTIterator(root)
# while i.hasNext(): print i.next()
