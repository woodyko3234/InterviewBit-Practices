class Solution:
    # @param A : string
    # @return an integer
    def isNumber(self, A):
        A = A.strip()
        n = len(A)
        if n == 0:
            return 0
        if A[0] == '+' or A[0] == '-':
            A = A[1:]
            n = n - 1
            if n == 0:
                return 0
        i = 0
        dotEncountered = False
        eEncountered = False
        while i < n:
            if '9' >= A[i] >= '0':
                i += 1
                continue
            if A[i] == '.':
                if dotEncountered:
                    return 0
                dotEncountered = True
                i += 1
                if i >= n:
                    return 0
                elif A[i] == 'e':
                    return 0
            elif A[i] == 'e':
                if eEncountered:
                    return 0
                eEncountered = True
                dotEncountered = True
                i += 1
                if i < n and (A[i] == '-' or A[i] == '+'):
                    i += 1
            else:
                return 0
        return 1
