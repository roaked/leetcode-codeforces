#Given an integer array sorted in non-decreasing order, there is exactly one integer in the array that occurs more than 25% of the time,
# return that integer.

# Beats 95.61% on Runtime / 74.56% on Memory

class Solution(object):
    def findSpecialInteger(self, arr: list):
        threshold = len(arr) // 4
        counter = 1
        for i in range(len(arr) - 1):
            if arr[i] == arr[i + 1]:
                counter += 1
                if counter > threshold:
                    return arr[i]
            else:
                counter = 1
        return arr[0]

arr = [1, 1]
print(Solution().findSpecialInteger(arr))

arr = [1, 2, 2, 6, 6, 6, 6, 7, 10]
print(Solution().findSpecialInteger(arr))