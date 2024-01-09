

from typing import List

class Solution:
    def findRelativeRanks(self, score: List[int]) -> List[str]:
        ans = []
        big = score.copy()
        big.sort(reverse=True)
        for i in range(len(score)):
            if score[i] == big[0]:
                ans.append('Gold Medal')
            elif score[i] == big[1]:
                ans.append('Silver Medal')
            elif score[i] == big[2]:
                ans.append('Bronze Medal')
            else:
                position = str(big.index(score[i]) + 1)
                if position == '4':
                    ans.append('4')
                else:
                    ans.append(position)
        return ans
    
print(Solution().findRelativeRanks(score = [10,3,8,9,4]))