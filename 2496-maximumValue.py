"""The value of an alphanumeric string can be defined as:

The numeric representation of the string in base 10, if it comprises of digits only.
The length of the string, otherwise.
Given an array strs of alphanumeric strings, return the maximum value of any string in strs."""

from typing import List
class Solution:
    def maximumValue(self, strs: List[str]) -> int:
        ans = []
        for string in strs:
            if string.isdigit(): #only digit
                ans.append(int(string))
                continue
            ans.append(len(string))     
        return max(ans)           

print(Solution().maximumValue(strs = ["alic3","bob","3","4","00000"]))