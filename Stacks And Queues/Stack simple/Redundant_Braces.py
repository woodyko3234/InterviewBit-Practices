class Solution:
    # @param A : string
    # @return an integer
    def braces(self, A):
        stack = list()
        got_operator = False
        for c in A:
            if c == '(':
                stack.append(c)
                got_operator = False
            elif c == ')':
                prev = stack.pop()
                if prev == '(':
                    return 1
                stack.pop()
                got_operator = False
            elif c in ('+', '*', '-', '/') and got_operator == False:
                stack.append('x')
                got_operator = True
        return 0
