'''
when target is lower than both left and right => trapped
so, check every valley, and how many units are trapped in it
how to define a valley?
for i in range(n):
    if A[i] >= A[i-1]: update left
    else: left is confirmed and stored, start to find right
'''

class Solution:
    # @param A : tuple of integers
    # @return an integer
    def trap(self, A):
        n = len(A)
        
        left = 0
        right = 0
        stack = []
        units = 0
        for i in range(n):
            if stack == []:
                #check and update left
                if (left == 0 and A[i] > 0) or (left < A[i]):
                    left = A[i]
                else:
                    stack.append(left)
                    target = A[i]
                    stack.append(target)
            elif right == 0:
                #update values before setting right
                if target >= A[i]:
                    target = A[i]
                    stack.append(target)
                else:
                    right = A[i]
                    stack.append(right)
            else:
                #update right
                if right <= A[i]:
                    right = A[i]
                    stack.append(right)
                else:
                    #the valley range is confirmed, should compute the units
                    valley = min(stack[0], stack[-1])
                    for j in stack[1:-1]:
                        if j < valley:
                            units += valley - j
                    #after done computation, reset right and stack
                    left = right
                    right = 0
                    stack = []
                    stack.append(left)
                    target = A[i]
                    stack.append(target)
        if stack and right:
            valley = min(stack[0], stack[-1])
            for j in stack[1:-1]:
                if j < valley:
                    units += valley - j
        return units
