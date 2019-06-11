class Solution:
	# @param dividend : integer
	# @param divisor : integer
	# @return an integer
	def divide(self, dividend, divisor):
	    isNegative = (dividend < 0) ^ (divisor < 0)
	    dividend = abs(dividend)
	    divisor = abs(divisor)
	    multiples = 1
	    while dividend >= (divisor << 1) :
	        divisor <<= 1
	        multiples <<= 1
	    result = 0
	    while multiples >= 1:
	        if dividend >= divisor:
	            dividend -= divisor
	            result += multiples
	        multiples >>= 1
	        divisor >>= 1
	    if isNegative:
	        return -result if -result > -2**31 else -2**31
	    else:
	        return result if result < 2**31 - 1 else 2**31 - 1
