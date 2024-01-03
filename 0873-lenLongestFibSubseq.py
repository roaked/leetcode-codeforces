"""A sequence x1, x2, ..., xn is Fibonacci-like if:

n >= 3
xi + xi+1 == xi+2 for all i + 2 <= n
Given a strictly increasing array arr of positive integers forming a sequence, 
return the length of the longest Fibonacci-like subsequence of arr. If one does not exist, return 0.

A subsequence is derived from another sequence arr by deleting any number of elements (including none) from arr,
 without changing the order of the remaining elements. For example, [3, 5, 8] is a subsequence of [3, 4, 5, 6, 7, 8]."""

class Solution:
    def lenLongestFibSubseq(self, arr: list[int]) -> int:
        ans = 0
        numbers = set(arr)
        n = len(arr)

        for i in range(n): #fix one value
            for j in range(i + 1, n): #check numbers after 
                a, b = arr[i], arr[j] 
                length = 2

                while a + b in numbers:
                    a, b = b, a + b # idea for Fibonacci
                    length += 1

                ans = max(ans, length)

        return ans if ans > 2 else 0

print(Solution().lenLongestFibSubseq(arr = [1,2,3,4,5,6,7,8]))

print(Solution().lenLongestFibSubseq(arr = [1,3,7,11,12,14,18]))