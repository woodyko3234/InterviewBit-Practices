class Solution:
    # @param A : integer
    # @return a strings
    def convertToTitle(self, A):
        #if A = 1=> chr(a) = chr(1 + 64) = 'A'
        chars = []
        while A > 0:
            if A%26 != 0:
                chars.append(A%26)
                A = A//26
            else:
                chars.append(26)
                A = A//26 - 1
        column = ''
        for char in chars[::-1]:
            column = column + chr(char + 64)
        return column
