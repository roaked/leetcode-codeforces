# Given an integer array nums, return all the triplets [nums[i], nums[j], nums[k]] such that 
#i != j, i != k, and j != k, and nums[i] + nums[j] + nums[k] == 0.

# Notice that the solution set must not contain duplicate triplets.
    #
class Solution(object):
    def threeSum(self, nums): # int[nums]  LIST
        nums.sort() # [-4, -1, -1, 0, 1, 2 ]  O(n log n) Avoiding duplicates
        number = len(nums) # number = 6
        result = [] # empty list
        for i in range(number - 2): # 1 in range (4) --> this way we skip the last 2 because we always move in triplets
            #check duplicates in first nº in triplet
            if i > 0 and nums[i] == nums[i - 1]:
                continue

            left, right = i + 1, number - 1  # left, right = 1, 5; RIGHT POINTER IS FIXED AT END OF LIST
            print(left, right)

            while left < right: # go through all the list (POINTERS)    i-1 <- (i) -> i+1    !! POINTER LEFT MUST START i+1 and then increase!! 
                total = nums[i] + nums[left] + nums[right] # total = nums[0] + nums[1] + nums[5] = -4-1+2=-3; -4-1+2=-3; -4+0+2=-2; -4+1+2=-1
                print(nums[i], nums[left], nums[right])
                if total < 0:
                    left += 1
                elif total > 0:
                    right -= 1
                else:
                    result.append([nums[i], nums[left], nums[right]])

                    # skip duplicates for 2nd nº in triplet ### MAYBE
                    while left < right and nums[left] == nums[left + 1]:
                        left += 1
                    # skip duplicates for 3rd nº in triplet ### MAYBE
                    while left < right and nums[right] == nums[right - 1]:
                        right -= 1

                    left += 1
                    right -= 1

        return result #

nums = [-1,0,1,2,-1,-4]
print(Solution().threeSum(nums))

nums = [0,1,1]
print(Solution().threeSum(nums))

nums = [0,0,0]
print(Solution().threeSum(nums))