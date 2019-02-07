class Solution:
    # @param A : integer
    # @return a list of strings
    def fizzBuzz(self, A):
        output = []
        if A <= 0: return output
        for i in range(1, A+1):
            if i % 3 == 0:
                if i % 5 == 0:
                    output.append('FizzBuzz')
                else:
                    output.append('Fizz')
            elif i % 5 == 0:
                output.append('Buzz')
            else:
                output.append(i)
        return output
