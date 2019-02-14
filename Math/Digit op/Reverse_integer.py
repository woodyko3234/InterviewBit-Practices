class Solution:
    # @param A : integer
    # @return an integer
    def reverse(self, A):
        X = list(str(A))
        if X[0] == '-':
            begin = 1
        else:
            begin = 0
        end = len(X) - 1
        while begin < end:
            X[begin], X[end] = X[end], X[begin]
            end -= 1
            begin += 1
        
        result = int("".join(X))
        if abs(result) > 2**31: return 0
        else: return result
