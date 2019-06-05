class Solution:
    # @param A : string
    # @return a list of strings
    def prettyJSON(self, A):
        prettierJson = []
        indentation = 0
        
        begin = 0
        for i in range(len(A)):
            if A[i] == ' ' and begin == i: 
                begin = i + 1
            elif A[i] == '{' or A[i] == '[':
                if i != begin:
                    prettierJson.append(('\t' * indentation) + A[begin: i])

                prettierJson.append(('\t' * indentation) + A[i])
                begin = i + 1
                indentation += 1
                
            elif A[i] == '}' or A[i] == ']':
                if i != begin:
                    prettierJson.append(('\t' * indentation) + A[begin: i])
                
                indentation -= 1
                if i+1 < len(A) and A[i+1] == ',':
                    prettierJson.append(('\t' * indentation) + A[i:i+2])
                    i += 1
                else:
                    prettierJson.append(('\t' * indentation) + A[i])
                begin = i + 1
            
            elif A[i] == ',' and i >= begin:
                prettierJson.append(('\t' * indentation) + A[begin: i+1])
                begin = i + 1
                
        return prettierJson
                    
