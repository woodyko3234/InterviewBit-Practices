class Solution:
    # @param A : string
    # @return string
    def reverseWords(self, A):
        #remove starting and ending spaces
        A = A.strip() 
        A = A.split(" ")
        output = []
        for i in A[::-1]:
            if i == "": continue
            else: output.append(i)
        return " ".join(output)
