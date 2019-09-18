class Solution:
    # @param arr : list of integers
    # @return a list of integers
    def prevSmaller(self, arr):
        length = len(arr)
        output = [-1] * length
        
        i = 0
        stack = []
        while i < length:
            cur = arr[i]
            for indice in stack[::-1]:
                if cur > indice:
                    output[i] = indice
                    break
            stack.append(cur)
            j = len(stack) - 2
            while j >= 0:
                if stack[j] > stack[-1]:
                    stack.pop(j)
                j -= 1
            i += 1
        return output
