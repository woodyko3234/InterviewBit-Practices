class Solution:
    # @param A : list of integers
    # @param B : integer
    # @param C : integer
    # @return an integer
    def solve(self, A, B, C):
        if not A: return 0
        elif C < 10**(B-1): return 0
        elif C > 10**B: 
            n = len(A)
            if A[0] == 0 and B > 1: return (n-1) * pow(n, B-1)
            else: return pow(n, B)
        elif B == 1: return len([i for i in A if i < C])
        else:
            n = len(A)
            T = str(C)
            output = 0
            for i in range(B):
                temp_lt = 0
                temp_eq = 0
                for j in A:
                    if j < int(T[i]): temp_lt += 1
                    elif j == int(T[i]): temp_eq = 1
                    else: break
                if i == 0 and A[0] == 0: output += (temp_lt-1) * pow(n, B-i-1)
                else: output += temp_lt * pow(n, B-i-1)
                if temp_eq == 0: break
        return output
