"""You are given a string s representing an attendance record for a student where each character signifies whether the student was absent,
 late, or present on that day. The record only contains the following three characters:

'A': Absent.
'L': Late.
'P': Present.
The student is eligible for an attendance award if they meet both of the following criteria:

C1 - The student was absent ('A') for strictly fewer than 2 days total.
C2 - The student was never late ('L') for 3 or more consecutive days.

Return true if the student is eligible for an attendance award, or false otherwise."""

class Solution:
    def checkRecord(self, s: str) -> bool:
        consectDays, absent = 0, 0

        for char in s:
            if char == 'A':
                absent += 1
                consectDays = 0  
                if absent >= 2:
                    return False
            elif char == 'L':
                consectDays += 1
                if consectDays >= 3:
                    return False
            else:
                consectDays = 0  

        return True
    
print(Solution().checkRecord(s = "PPALLP"))
print('\n')
print(Solution().checkRecord(s = "PPALLL"))
