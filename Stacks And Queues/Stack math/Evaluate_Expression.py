'''
  ["2", "1", "+", "3", "*"] -> ((2 + 1) * 3) -> 9
  ["4", "13", "5", "/", "+"] -> (4 + (13 / 5)) -> 6
  [ "5", "1", "2", "+", "4", "*", "+", "3", "-" ] -> (5 + ((1+2) * 4) - 3) = 14
'''

class Solution:
    # @param A : list of strings
    # @return an integer
    def evalRPN(self, A):
        manipulation = []
        for i in A:
            try:
                cur = int(i)
                manipulation.append(cur)
            except:
                if i == '+':
                    comp = manipulation[-2] + manipulation[-1]
                elif i == '-':
                    comp = manipulation[-2] - manipulation[-1]
                elif i == '*':
                    comp = manipulation[-2] * manipulation[-1]
                elif i == '/':
                    comp = manipulation[-2] / manipulation[-1]
                else:
                    return -1
                manipulation[-2] = comp
                manipulation.pop()
        return manipulation[0]
