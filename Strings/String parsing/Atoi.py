class Solution:
    # @param A : string
    # @return an integer
    def atoi(self, A):
        start = 0
        if len(A) == 0 : return 0
        elif (A[start] != '-' and A[start] != '+') and (not A[start].isdigit()): 
            return 0
        else:
            max_atoi = A[0]
            for i in range(1, len(A)):
                if A[i].isdigit():
                    max_atoi += A[i]
                else:
                    try:
                        if int(max_atoi) >= 2147483648:
                            return 2147483647
                        elif int(max_atoi) <= -2147483648:
                            return -2147483648
                        else:
                            return int(max_atoi)
                    except:
                        return 0
            try:
                if int(max_atoi) >= 2147483648:
                    return 2147483647
                elif int(max_atoi) <= -2147483648:
                    return -2147483648
                else:
                    return int(max_atoi)
            except:
                return 0
