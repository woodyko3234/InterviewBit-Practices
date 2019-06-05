class Solution:
    # @param A : string
    # @param B : integer
    # @return a strings
    def convert(self, A, B):
        #if B = 4, A = 'abcdefghijk':
        #pattern is: A[0] + A[6] + A[12]
        #[A[i], A[i+(2*(B-1))]
        #B = 2 => [A[0], A[2]]; B = 3 => [A[0], A[4]]
        if B == 1: return A
        pattern = B - 1
        a_len = len(A)
        a_split = []
        for i in range(0, a_len, 2*pattern):
            if i + (2*pattern) <= a_len:
                a_split.append(A[i: (i+2*pattern)])
            else:
                a_split.append(A[i:])
        
        reorder = ""
        baseline = 0
        while baseline < B:
            if baseline == 0:
                for i in range(len(a_split)):
                    reorder += a_split[i][baseline]
            elif 0 < baseline < (B-1):
                for i in range(len(a_split)):
                    if len(a_split[i]) == 2*pattern:
                        reorder += a_split[i][baseline]
                        reorder += a_split[i][-baseline]
                    else:
                        try:
                            reorder += a_split[i][baseline]
                            reorder += a_split[i][baseline + 2*(pattern-baseline)]
                        except: pass
            else:
                for i in range(len(a_split)):
                    try:
                        reorder += a_split[i][baseline]
                    except: pass
            baseline += 1
        return reorder
