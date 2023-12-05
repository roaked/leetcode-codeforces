# Given an integer array nums, return all the triplets [nums[i], nums[j], nums[k]] such that 
#i != j, i != k, and j != k, and nums[i] + nums[j] + nums[k] == 0.

# Notice that the solution set must not contain duplicate triplets.

class Solution(object):
    def threeSum(self, nums): # int[nums]  LIST
        nums.sort() # [-4, -1, -1, 0, 1, 2 ]
        number = len(nums) # 
        result = []
        for i in range(number - 2):
        #duplicates
            if i > 0 and nums[i] == nums[i - 1]:
                continue

        left, right = i + 1, n - 1  # Pointers for the other two numbers

        while left < right:
            total = nums[i] + nums[left] + nums[right]

            if total < 0:
                left += 1
            elif total > 0:
                right -= 1
            else:
                result.append([nums[i], nums[left], nums[right]])

                # Skip duplicate values for the second number in the triplet
                while left < right and nums[left] == nums[left + 1]:
                    left += 1
                # Skip duplicate values for the third number in the triplet
                while left < right and nums[right] == nums[right - 1]:
                    right -= 1

                left += 1
                right -= 1

        return result

nums = [-1,0,1,2,-1,-4]
print(Solution().threeSum(nums))

nums = [0,1,1]
print(Solution().threeSum(nums))

nums = [0,0,0]
print(Solution().threeSum(nums))