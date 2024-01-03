class Solution:
    def removeDuplicates(self, nums: list[int]) -> int:
        if not nums:
            return 0
        
        index = 1 
        
        for i in range(1, len(nums)):
            if nums[i] != nums[i - 1]:
                nums[index] = nums[i]
                index += 1
        
        return index

    def removeDuplicatesSet(self, nums: list[int]) -> int:
        nums[:] = sorted(set(nums)) 
        return len(nums)

sol = Solution()
print(sol.removeDuplicates(nums=[1, 1, 2])) 
print(sol.removeDuplicates(nums=[0, 0, 1, 1, 1, 2, 2, 3, 3, 4])) 
print(sol.removeDuplicates(nums=[0, 1, 2, 2, 2, 2, 2, 3, 4, 4, 4])) 
print(sol.removeDuplicates(nums=[1, 1, 1, 1, 1]))  