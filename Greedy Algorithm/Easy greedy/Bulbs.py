class Solution:
    # @param A : list of integers
    # @return an integer
    def bulbs(self, A):
        n = len(A)
        flips = 0
        coinFlip = True #True => check 0, False => check 1
        for i in range(n):
            if A[i] == 1 and coinFlip: continue #OK
            elif A[i] == 0 and coinFlip:
                #FLIPA!!
                flips += 1
                coinFlip = False #now we flip when meeting 1
            elif A[i] == 1:
                #coinFlip == False, FLIP!
                flips += 1
                coinFlip = True
        return flips
