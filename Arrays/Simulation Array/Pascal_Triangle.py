class Solution:
    # @param A : integer
    # @return a list of list of integers
    def generate(self, A):
        if A == 0: return []
        output = []
        for i in range(1, A+1):
            appending = [0] * i
            output.append(appending)
        #set all left and right borders to be 1
        for i in range(len(output)):
            output[i][0] = 1
            output[i][-1] = 1
        #return if no inside contents needed to be updated
        if len(output) <= 2: return output     
        
        #fill out contents inside
        row = 2 #start at third row
        while row < len(output):
            for i in range(1, len(output[row]) - 1):
                #exclude indice 0 and -1 in every row
                output[row][i] = output[row-1][i-1]+output[row-1][i]
            row += 1
        return output
        
