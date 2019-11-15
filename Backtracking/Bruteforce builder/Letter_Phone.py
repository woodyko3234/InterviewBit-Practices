class Solution:
    # @param A : string
    # @return a list of strings
    def letterCombinations(self, A):
        letters = ""
        comb = []
        alphabets = {'0': ['0'], '1': ['1'], '2':['a','b','c'], 
                  '3':['d','e','f'], '4':['g','h','i'],
                  '5':['j','k','l'], '6':['m','n','o'],
                  '7':['p','q','r','s'], '8':['t','u','v'],
                  '9':['w','x','y','z']}
        i = 0
        n = len(A)
        
        self.recursive(A,i,n,letters,comb,alphabets)
        
        return comb
        
        
    def recursive(self, A, i, n, letters, comb, alphabets):
        if i < n:
            for choice in alphabets[A[i]]:
                self.recursive(A, i+1, n, letters+choice, comb, alphabets)
        if i == n: #create unnecessary strings, how to avoid?
            comb.append(letters)
        return 
