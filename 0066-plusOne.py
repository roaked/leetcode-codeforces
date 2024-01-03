"""
You are given a large integer represented as an integer array digits, where each digits[i] is the ith digit of the integer.
The digits are ordered from most significant to least significant in left-to-right order. The large integer does not contain any leading 0's.
Increment the large integer by one and return the resulting array of digits.
"""

class Solution(object):
    def plusOne(self, digits: list[int]) -> list[int]:
        n = len(digits)
        for i in range(n - 1, -1, -1):
            # If the digit is less than 9, increment it and return the digits
            if digits[i] < 9:
                digits[i] += 1
                return digits
            # If the digit is 9, set it to 0 and continue to the next digit
            digits[i] = 0     
        # If all digits were 9, add a new digit '1' at the beginning
        return [1] + digits
   

digits = [1,2,3]
print(Solution().plusOne(digits))

digits = [4,3,2,1]
print(Solution().plusOne(digits))

digits = [9]
print(Solution().plusOne(digits))