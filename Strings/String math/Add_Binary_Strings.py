class Solution:
    # @param A : string
    # @param B : string
    # @return a strings
    def addBinary(self, A, B):
        AplusB = list(str(int(A) + int(B)))
        length = len(AplusB)
        
        idx = length - 1
        while idx >= 0:
            if int(AplusB[idx]) // 2 == 1:
                AplusB[idx] = '%d' % (int(AplusB[idx]) - 2)
                if idx - 1 >= 0:
                    if AplusB[idx-1] == '1':
                        AplusB[idx-1] = '2'
                    elif AplusB[idx-1] == '2':
                        AplusB[idx-1] = '3'
                    else:
                        AplusB[idx-1] = '1'
                else:
                    AplusB = ['1'] + AplusB
            idx -= 1
        return "".join(AplusB)
