"""Given an array of integers arr, and three integers a, b and c. You need to find the number of good triplets.

A triplet (arr[i], arr[j], arr[k]) is good if the following conditions are true:

0 <= i < j < k < arr.length
|arr[i] - arr[j]| <= a
|arr[j] - arr[k]| <= b
|arr[i] - arr[k]| <= c
Where |x| denotes the absolute value of x.

Return the number of good triplets."""

class Solution:
    def countGoodTriplets(self, arr: list[int], a: int, b: int, c: int) -> int:
        cnt, debug = 0, []

        for i in range(len(arr)):
            for j in range(i + 1, len(arr)):
                for k in range(j + 1, len(arr)):
                    if(0 <= i < j < k < len(arr)):
                        if (abs(arr[i] - arr[j]) <= a) and (abs(arr[j] - arr[k]) <= b) and (abs(arr[i] - arr[k]) <= c):
                            cnt += 1
                            debug.append([arr[i], arr[j], arr[k]])
        return cnt, debug

print(Solution().countGoodTriplets(arr = [3,0,1,1,9,7], a = 7, b = 2, c = 3))

print(Solution().countGoodTriplets(arr = [7,3,7,3,12,1,12,2,3], a = 5, b = 8, c = 1))