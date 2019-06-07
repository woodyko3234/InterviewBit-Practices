class Solution:
    # @param A : string
    # @return a list of strings
    def prettyJSON(self, A):
        prettier = []
        indentNum = 0
        temp = ""
        for i in A:
            if i == " ": continue
            temp += i
            if (i == '[' or i == '{'):
                if temp != i:
                    prettier.append("\t" * indentNum + temp[:-1])
                    temp = i
                prettier.append("\t" * indentNum + temp)
                indentNum += 1
                temp = ""
            elif i == ',':
                prettier.append("\t" * indentNum + temp)
                temp = ""
            elif i == ']' or i == '}':
                if temp != i:
                    prettier.append("\t" * indentNum + temp[:-1])
                    temp = i
                indentNum -= 1
                #prettier.append("\t" * indentNum + temp)
                #temp = ""
        prettier.append("\t" * indentNum + temp)
        return prettier
