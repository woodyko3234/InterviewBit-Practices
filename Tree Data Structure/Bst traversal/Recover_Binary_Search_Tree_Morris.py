class Solution:
    # @param A : root node of tree
    # @return a list of integers
    def recoverTree(self, A):
        self.first = None
        self.prev = None
        self.last = None
        self.traverse(A)
        return([self.last, self.first])
    
    def traverse(self, A):
        if(A.left is not None):
            self.traverse(A.left)
        if(self.prev is not None and self.prev > A.val):
            if(self.first is None):
                self.first = self.prev
                self.last = A.val
            else:
                self.last = A.val
        self.prev = A.val
        if(A.right is not None):
            self.traverse(A.right)
