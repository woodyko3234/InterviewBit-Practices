class Solution:
	# @param A : list of strings
	# @return an integer
	def evalRPN(self, A):
        """
        [55, 2, 3, +, /] => (55)/((2)+(3))
        [2, 1, +, 3, *] => ((2)+(1))*(3)
        [55, *, 2, +, 3] => Invalid
        """
        toOperate = []
        operators = ["+", "-", "*", "/"]
        for e in A:
            if e not in operators:
                toOperate.append(int(e))
            else:
                opTwo = toOperate.pop()
                opOne = toOperate.pop()
                if e == "+":
                    toOperate.append(opOne + opTwo)
                elif e == "-":
                    toOperate.append(opOne - opTwo)
                elif e == "*":
                    toOperate.append(opOne * opTwo)
                elif e == "/":
                    toOperate.append(opOne // opTwo)
        return toOperate.pop()
