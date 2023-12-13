"""Given an array of distinct integers candidates and a target integer target, return a list of all unique combinations of candidates 
where the chosen numbers sum to target. You may return the combinations in any order.

The same number may be chosen from candidates an unlimited number of times. Two combinations are unique if the 
frequency of at least one of the chosen numbers is different.

The test cases are generated such that the number of unique combinations that sum up to target is less than 150 combinations for the given input."""

class Solution:
    def combinationSum(self, candidates: list[int], target: int) -> list[list[int]]:
        sol = []
        candidates.sort()
        for candidate in candidates[::-1]:
            if candidate > target:
                candidates.pop()
            elif candidate == target:
                sol.append([candidate])
                candidates.pop()
                break
            else:
                continue
        #print(sol) [7]
        #print(candidates) [2, 3, 6]
        size = len(candidates) #3

        def dfs(combination, current_sum, idx):
            if current_sum > target: 
                return
            if current_sum == target: 
                sol.append(combination)
            for i in range(idx, size): 
                dfs(combination + [candidates[i]], current_sum + candidates[i], i)
        
        dfs([],0,0)
        return sol
    
        # for i in range(size): #0,1,2
        #     print(i)
        #     while candidates[i+1]:
        #         if candidates[i] + candidates[i+1] > target: continue
        #         elif candidates[i] + candidates[i+1] == target: sol.append(candidates[i])

candidates = [2,3,6,7]
target = 7
print(Solution().combinationSum(candidates,target))

candidates = [2,3,5]
target = 8
print(Solution().combinationSum(candidates,target))

candidates = [2]
target = 1
print(Solution().combinationSum(candidates,target))