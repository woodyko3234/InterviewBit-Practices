class Solution:
    # @param A : integer
    # @return a list of strings
    def generateParenthesis(self, A):
        left = 0
        right = 0
        word = ""
        comb = []
        
        self.recursive(A, word, comb, left, right)
        
        return comb
        
    def recursive(self, A, word, comb, left, right):
        if left == 0 or (left == right and left < A):
            self.recursive(A, word + '(', comb, left + 1, right)
        elif A > left > 0 and left > right:
            self.recursive(A, word + '(', comb, left + 1, right) or \
            self.recursive(A, word + ')', comb, left, right + 1)
        elif left == A and right < A:
            self.recursive(A, word + ')', comb, left, right + 1)
        if left + right == 2*A:
            comb.append(word)
        return 
