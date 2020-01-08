from bisect import bisect_left
class Solution:
    # @param A : list of integers
    # @param B : list of integers
    # @return a list of integers
    def solve(self, A, B):
        """
        Must try combining query 1 & 2, 
        that will reduce memory requirement a lot
        """
        frequencies = self.getFrequency(A)
        n, proA = len(A), []
        #query 3
        for i in range(n):
            proA.append(self.divisorProduct(A[i]))
        fA = list(zip(proA, frequencies))
        fA.sort(reverse = True)
        V, accumulated = [], 0
        for i in range(n):
            accumulated += fA[i][1]
            V.append(accumulated)
        output = []
        for i in B:
            output.append(fA[bisect_left(V, i)][0])
        #query 5
        return output

    def getFrequency(self, A):
        n = len(A)
        L, R = [1] * n, [1] * n
        S, top = [], -1
        for i in range(n):
            while(top >= 0 and A[S[top]] <= A[i]):
                S.pop()
                top -= 1
            if (top >= 0):
                L[i] = i - S[top]
            else:
                L[i] = i + 1
            S.append(i)
            top += 1
        S = []
        top = -1
        for i in range(n-1, -1, -1):
            while(top >= 0 and A[S[top]] < A[i]):
                S.pop()
                top -= 1
            if (top >= 0):
                R[i] = S[top] - i
            else:
                R[i] = n - i
            S.append(i)
            top += 1
        for i in range(n):
            L[i] *= R[i]
        return L
        
    def divisorProduct(self, k):
        d = 2
        for i in range(2, int(k**0.5)+1):
            if k % i == 0:
                if k//i != i:
                    d += 1
                d += 1
        output = 1
        for _ in range(d // 2):
            output = (output * k) % (10**9 + 7)
        if d % 2 != 0:
            output = (output * (k**0.5)) % (10**9 + 7)
        return int(output)
