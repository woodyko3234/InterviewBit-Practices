class Solution:
    # @param A : string
    # @return an integer
    def seats(self, A):
        """
        Main Question: How to find the positions which require minimum movements?
        Bruteforce: try to set every seat as the center,
                    and see how many movements each needs.
        Smart: find the median?!
        """
        minMove, n, MOD = float("inf"), len(A), 1e7+3
        occupied = []
        if n <= 1: return 0
        for i in range(n):
            if A[i] == 'x': occupied.append(i)
        m = len(occupied)
        if m <= 1: return 0
        #find median/medians
        medians = [m//2]
        for j in medians:
            center = occupied[j]
            jL = center-1 #rightmost unoccupied position next to index j on the left
            jR = center+1 #leftmost unoccupied position next to index j on the right
            tempM = 0 #summation of movements
            if j == 0: pass
            else:
                for k in occupied[j-1::-1]:
                #left side movements
                    tempM += ((jL-k) % MOD)
                    jL -= 1
            if j == m-1: pass
            else:
                for k in occupied[j+1:]:
                    tempM += ((k-jR) % MOD)
                    jR += 1
            #update minMove
            if minMove > tempM:
                minMove = tempM % MOD
        return int(minMove)

        
