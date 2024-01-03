"""Given an integer array nums, return all the triplets [nums[i], nums[j], nums[k]] such that 
#i != j, i != k, and j != k, and nums[i] + nums[j] + nums[k] == 0.

# Notice that the solution set must not contain duplicate triplets."""

class Solution(object):
    def threeSum(self, nums: list): 
        nums.sort() 
        number = len(nums) 
        result = []
        for i in range(number - 2): # 1 in range (4) --> this way we skip the last 2 because we always move in triplets
            #check duplicates in first nº in triplet
            if i > 0 and nums[i] == nums[i - 1]:
                continue 

            l, r = i + 1, number - 1  # l, r = 1, 5; r pointer at end of list
            print(l, r)

            while l < r: # go through list w/ pointers   i-1 <- (i) -> i+1
                total = nums[i] + nums[l] + nums[r] 
                print(nums[i], nums[l], nums[r])
                if total < 0:
                    l += 1
                elif total > 0:
                    r -= 1
                else:
                    result.append([nums[i], nums[l], nums[r]])

                    # skip duplicates for 2nd nº in triplet ### MAYBE
                    while l < r and nums[l] == nums[l + 1]:
                        l += 1
                    # skip duplicates for 3rd nº in triplet ### MAYBE
                    while l < r and nums[r] == nums[r - 1]:
                        r -= 1
                    l += 1
                    r -= 1

        return result 

nums = [-1,0,1,2,-1,-4]
print(Solution().threeSum(nums))

nums = [0,1,1]
print(Solution().threeSum(nums))

nums = [0,0,0]
print(Solution().threeSum(nums))