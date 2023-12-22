"""A permutation perm of n + 1 integers of all the integers in the range [0, n] can be represented as a string s of length n where:

s[i] == 'I' if perm[i] < perm[i + 1], and
s[i] == 'D' if perm[i] > perm[i + 1].
Given a string s, reconstruct the permutation perm and return it. If there are multiple valid permutations perm, return any of them."""

class Solution:
    def diStringMatch(self, s: str) -> list[int]:
        per, lower, upper = [], 0, len(s)
        
        for i in s:
            if i == 'I':
                per.append(lower)
                lower += 1
            else:
                per.append(upper)
                upper -= 1
        
        per.append(lower) if s[-1] == 'I' else per.append(upper)

        return per


print(Solution().diStringMatch(s = "IDID"))
print('\n')
print(Solution().diStringMatch(s = "III"))
print('\n')
print(Solution().diStringMatch(s = "DDI"))
print('\n')
