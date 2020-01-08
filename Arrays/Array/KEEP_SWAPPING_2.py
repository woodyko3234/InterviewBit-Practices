class Solution:
    # @param A : string
    # @param B : string
    # @param C : integer
    # @return a strings
    def solve(self, A, B, C):
        n = len(A)
        if C == n: return A
        B = int(B) + 1 #swap int(B) +1 times in total
        sol = ['_'] * n
        #why the loop is narrowed to C, instead of B?
        #bcz only in this range we can make sure the characters
        #are just kept swapped while the loop is processing
        for i in range(C):
            #steps: compute how many times it would be swapped
            steps = B // C + (1 if B % C > i else 0)
            #loc: the final location after all swaps
            loc = (i + C * steps) % n
            sol[loc] = A[i]

        #So, how can we get the locations of the rest char?
        offset = B // n * C + max(0, B % n + C - n)
        #offset: how many times other chars get swapped
        j = 0
        #allocate the rest of chars
        A = A[C:]
        for i in range(n):
            if sol[i] == '_':
                sol[i] = A[(j + offset) % len(A)]
                j += 1
        return ''.join(sol)
