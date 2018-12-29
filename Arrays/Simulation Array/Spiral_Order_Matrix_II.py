class Solution:
    # @param A : integer
    # @return a list of list of integers
    def generateMatrix(self, A):
        if A <= 0: return [[]]
        elif A == 1: return [[1]]
        bot = A - 1
        right = A - 1
        top = 0
        left = 0
        output = []
        for i in range(A):
            output.append([0] * A)
        indice = 1
        total_indices = A * A
        
        while indice <= total_indices:
            #top border
            for i in range(left, right + 1):
                output[top][i] = indice
                indice += 1
            top += 1
            
            if indice > total_indices: break
            #right border
            for i in range(top, bot + 1):
                output[i][right] = indice
                indice += 1
            right -= 1
            
            if indice > total_indices: break
            
            #bot border
            for i in range(right, left - 1, -1):
                output[bot][i] = indice
                indice += 1
            bot -= 1
            
            if indice > total_indices: break
        
            #left border
            for i in range(bot, top - 1, -1):
                output[i][left] = indice
                indice += 1
            left += 1
        
        return output
