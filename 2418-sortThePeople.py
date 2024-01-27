"""You are given an array of strings names, and an array heights that consists of distinct positive integers.
 Both arrays are of length n.

For each index i, names[i] and heights[i] denote the name and height of the ith person.

Return names sorted in descending order by the people's heights."""

from typing import List
class Solution:
    def sortPeople(self, names: List[str], heights: List[int]) -> List[str]:
        t = [[names[_],heights[_]] for _ in range(len(names))] 
        a = sorted(t, reverse = True, key = lambda x: x[1])
        return [a[_][0] for _ in range(len(a))]
        


print(Solution().sortPeople(names = ["Mary","John","Emma"], heights = [180,165,170]))