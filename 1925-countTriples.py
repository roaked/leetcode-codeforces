"""A square triple (a,b,c) is a triple where a, b, and c are integers and a2 + b2 = c2.

Given an integer n, return the number of square triples such that 1 <= a, b, c <= n."""

import math
class Solution:
    def countTriples(self, n: int) -> int:
        cnt = 0
        for i in range(1, n+1):
            for j in range(i+1, n+1):
                k = i*i + j*j
                if k > n*n: break
                if math.sqrt(k) % 1 == 0:
                    cnt += 1
        return cnt * 2


print(Solution().countTriples(n = 5))