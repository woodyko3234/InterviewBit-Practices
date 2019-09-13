class Solution:
    # @param A : string
    # @return an integer
    def braces(self, A):
        stack = list()
        for c in A:
            if c == '(':
                stack.append(c)
            elif c == ')':
                prev = stack.pop()
                if prev == '(':
                    return 1
                stack.pop()
            elif c in ('+', '*', '-', '/'):
                stack.append('x')

        return 0
