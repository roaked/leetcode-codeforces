"""Given an array of distinct integers candidates and a target integer target, return a list of all unique combinations of candidates 
where the chosen numbers sum to target. You may return the combinations in any order.

The same number may be chosen from candidates an unlimited number of times. Two combinations are unique if the 
frequency of at least one of the chosen numbers is different.

The test cases are generated such that the number of unique combinations that sum up to target is less than 150 combinations for the given input."""

class Solution(object):
    def combinationSum(self, candidates: list[int], target: int) -> list[list[int]]: #Better than 99% Run time + 91% Memory
        sol = []
        candidates.sort(reverse=True) # bigger first
        for i in range(len(candidates)-1,-1,-1):
            candidate = candidates[i]
            if candidate > target:
                candidates.pop(i)  
            elif candidate == target:
                sol.append([candidate])
                candidates.pop(i) 
                break
            elif candidate <= 0:
                candidates.pop(i)  #zero or negative
            else:
                continue

        SIZE = len(candidates)
        def dfs(combination, current_sum, idx):
            if current_sum > target or current_sum < 0: #technically < 0 already secured previously
                return
            if current_sum == target: 
                sol.append(combination)
            for i in range(idx, SIZE): 
                dfs(combination + [candidates[i]], current_sum + candidates[i], i)
        dfs([],0,0)
        return sol

candidates = [2,3,6,7]
target = 7
print(Solution().combinationSum(candidates,target))

candidates = [2,3,5]
target = 8
print(Solution().combinationSum(candidates,target))

candidates = [2]
target = 1
print(Solution().combinationSum(candidates,target))

candidates = [7,0,-1,1,2,3,4]
target = 7
print(Solution().combinationSum(candidates,target))