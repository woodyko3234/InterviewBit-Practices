from math import factorial
class Solution:
    # @param A : string
    # @return an integer
    def findRank(self, A):
        rank = 1
        n = len(A)
        letter_ord = [ord(i) for i in A]
        #print(letter_ord)
        for i, c in enumerate(A):
            cur = letter_ord[i]
            cur_rank = 0
            for j in range(i+1, n):
                if letter_ord[i] > letter_ord[j]: cur_rank +=1
            #print(cur)
            rank += cur_rank * factorial(n-i-1)
            if rank > 1000003:
                rank = rank % 1000003    
        return rank
