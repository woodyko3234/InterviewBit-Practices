from collections import defaultdict, Counter
class Solution:
	# @param A : tuple of strings
	# @return a list of list of integers
    def anagrams(self, A):
        output = []
        anagramDict = defaultdict(list)
        for i in range(len(A)):
            counter = tuple(sorted(Counter(A[i]).items()))
            anagramDict[counter].append(i+1)
        for val in anagramDict.values():
            output.append(val)
        return (output)
