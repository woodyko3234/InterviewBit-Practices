class Solution:
    # @param A : string
    # @return an integer
    def atoi(self, A):
        A_split = A.split()
        for i in A_split:
            if not i: continue
            output = 0
            minus = False
            if i[0] == "-": minus = True
            for j in range(len(i)):
                if j == 0 and (i[j] == "-" or i[j] == "+"): continue
                if i[j].isnumeric():
                    if minus:
                        output = output * 10 - int(i[j])
                        if output < (-1 * (2**31)): return -1 * (2**31)
                    else:
                        output = output * 10 + int(i[j])
                        if output > (2**31 - 1): return 2**31 - 1
                else: return output
            if output != 0: return output
            else: return 0
        return 0    
