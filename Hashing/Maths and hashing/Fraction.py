from collections import defaultdict
class Solution:
	# @param A : integer
	# @param B : integer
	# @return a strings
    def fractionToDecimal(self, A, B):
        if A % B == 0: return str(A//B)
        neg = False
        if (A<0 or B<0) and not (A<0 and B<0): 
            neg = True
            A, B = abs(A), abs(B)
        intstr = str(A//B)
        modularDict = defaultdict(bool)
        modularIdx, decimalIdx = {}, 0
        modular = A%B
        decimals = []
        while modularDict[modular] == False and modular != 0:
            modularDict[modular] = True
            modularIdx[modular] = decimalIdx
            decimalIdx += 1
            modular *= 10
            decimals.append(str(modular//B))
            modular = modular % B
        if modularDict[modular]:
            #divide into before and in the brackets
            beforeBra = "".join(decimals[:modularIdx[modular]])
            inBra = "("+"".join(decimals[modularIdx[modular]:])+")"
            decimals = [beforeBra, inBra]
        if neg:
            return "-"+intstr+"."+"".join(decimals)
        return intstr+"."+"".join(decimals)
