class Solution:
    # @param A : list of integers
    # @return a list of integers
    def wave(self, A):
        if len(A) == 0: return []
        elif len(A) == 1: return A
        result = []
        a_len = len(A)
        A = sorted(A)
        for i in range(1, a_len-1):
            if i % 2 == 1 and A[i-1] >= A[i]:
                result.append(A[i-1])
            elif i % 2 == 1 and A[i-1] < A[i]:
                A[i], A[i-1] = A[i-1], A[i]
                result.append(A[i-1])
            elif i % 2 == 0 and A[i-1] <= A[i]:
                result.append(A[i-1])
            elif i % 2 == 0 and A[i-1] > A[i]:
                A[i], A[i-1] = A[i-1], A[i]
                result.append(A[i-1])
        current = A[a_len - 2]
        nextt = A[a_len - 1]
        if (a_len - 2) % 2 == 1 and current <= nextt:
            result.append(current)
            result.append(nextt)
        elif (a_len - 2) % 2 == 1 and current > nextt:
            current, nextt = nextt, current
            result.append(current)
            result.append(nextt)
        if (a_len - 2) % 2 == 0 and current >= nextt:
            result.append(current)
            result.append(nextt)
        elif (a_len - 2) % 2 == 0 and current < nextt:
            current, nextt = nextt, current
            result.append(current)
            result.append(nextt)    

        return result
                
