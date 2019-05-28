class Solution:
    # @param A : integer
    # @return a strings
    def intToRoman(self, A):

        a_str = str(A)
        digits = len(a_str)
        roman = ""
        idx = 0
        while digits > 0:
            cur_int = int(a_str[idx])
            if digits == 4:
                roman += 'M' * cur_int
            elif digits == 3:
                if cur_int == 9:
                    roman += 'CM'
                elif 5 <= cur_int < 9:
                    roman += ('D' + 'C' * (cur_int - 5))
                elif cur_int == 4:
                    roman += 'CD'
                else:
                    roman += 'C' * cur_int
            elif digits == 2:
                if cur_int == 9:
                    roman += 'XC'
                elif 5 <= cur_int < 9:
                    roman += ('L' + 'X' * (cur_int - 5))
                elif cur_int == 4:
                    roman += 'XL'
                else:
                    roman += 'X' * cur_int
            elif digits == 1:
                if cur_int == 9:
                    roman += 'IX'
                elif 5 <= cur_int < 9:
                    roman += ('V' + 'I' * (cur_int - 5))
                elif cur_int == 4:
                    roman += 'IV'
                else:
                    roman += 'I' * cur_int
            idx += 1
            digits -= 1
        return roman
