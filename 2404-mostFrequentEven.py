"""Given an integer array nums, return the most frequent even element.

If there is a tie, return the smallest one. If there is no such element, return -1."""

from typing import List
from collections import Counter

class Solution:
    def mostFrequentEven(self, nums: List[int]) -> int:
        d = Counter(filter(lambda x: x % 2 == 0, nums))
        return max(d.keys(), key = lambda x: (d[x], -x), default = -1)
    
print(Solution().mostFrequentEven(nums = [4287,799,8103,3526,8396,7060,8287,4214,4093,6763,651,4907,8350,4866,5114,5245,3198,6644,3620,1586,3068,2769,9506,2319,588,5055,730,6968,4814,144,5180,8798,8783,3319,7765,3254,7164,5462,8085,5481,8363,3135,2910,583,3751,3044,8734,4075,5489,7866,3404,9532,3751,571,7460,4934,9346,4076,1505,9576,9406,3342,8090,5979,3140,4453,4779,9324,2945,7279,6809,9619,6958,9881,8308,9246,2529,3727,1241,7230,4536,9852,1667,1688,1320,6400,6359,6140,904,6287,6499,9256,7666,4083,2927,3165,9239,9433,1620,6961,3115,8766,2416,6653,9030,2690,9165,6150,1644,5925]))
print(Solution().mostFrequentEven(nums = [0,1,2,2,4,4,1]))