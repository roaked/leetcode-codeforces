"""You are given a string s consisting only of the characters '0' and '1'. In one operation, you can change any '0' to '1' or vice versa.

The string is called alternating if no two adjacent characters are equal. For example, the string "010" is alternating, while the string "0100" is not.

Return the minimum number of operations needed to make s alternating."""


class Solution:
    def minOperations(self, s: str) -> int:
        s0, s1 = 0, 0      
          
        for i in range(len(s)):
            if i % 2 == 0:
                if s[i] == "0":
                    s1 += 1
                else:
                    s0 += 1
            else:
                if s[i] == "1":
                    s1 += 1
                else:
                    s0 += 1
        
        return min(s0, s1)
    
print(Solution().minOperations(s = "0100")) #1
print('\n')
print(Solution().minOperations(s = "10")) #0
print('\n')
print(Solution().minOperations(s = "1111")) #2