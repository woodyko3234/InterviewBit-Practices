class Solution:
    # @param A : string
    # @return an integer
    def romanToInt(self, A):
        A = A + ' '
        a_len = len(A)
        num = 0
        for i in range(a_len):
            if A[i] == 'M':
                num += 1000
            elif A[i] == 'C':
                if A[i+1] == 'M' or A[i+1] == 'D':
                    num -= 100
                else:
                    num += 100
            elif A[i] == 'D':
                num += 500
            elif A[i] == 'X':
                if A[i+1] == 'C' or A[i+1] == 'L':
                    num -= 10
                else:
                    num += 10
            elif A[i] == 'L':
                num += 50
            elif A[i] == 'I':
                if A[i+1] == 'X' or A[i+1] == 'V':
                    num -= 1
                else:
                    num += 1
            elif A[i] == 'V':
                num += 5
            else: continue
        return num
