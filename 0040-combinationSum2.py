"""Given a collection of candidate numbers (candidates) and a target number (target), 
find all unique combinations in candidates where the candidate numbers sum to target.

Each number in candidates may only be used once in the combination.

Note: The solution set must not contain duplicate combinations."""

class Solution:
    def combinationSum2(self, candidates: list[int], target: int) -> list[list[int]]:
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

        #print(candidates)      
        SIZE = len(candidates)  

        def dfs(combination, current_sum, idx):
            if current_sum > target or current_sum < 0: #technically < 0 already secured previously
                return
            if current_sum == target: 
                sol.append(combination)
                return 
            for i in range(idx, SIZE): #[1,2,5,6,7] but in reverse
                if i > idx and candidates[i] == candidates[i - 1]:
                    continue
                dfs(combination + [candidates[i]], current_sum + candidates[i], i + 1)
        dfs([],0,0)
        unique_sol = list(map(list, set(map(tuple, sol)))) #return unique
        return unique_sol
    
candidates = [10,1,2,7,6,1,5]
target = 8
print(Solution().combinationSum2(candidates,target))

candidates = [2,5,2,1,2]
target = 5
print(Solution().combinationSum2(candidates,target))

candidates = [1,1]
target = 1
print(Solution().combinationSum2(candidates,target))

candidates = [7,0,-1,1,2,3,4]
target = 7
print(Solution().combinationSum2(candidates,target))