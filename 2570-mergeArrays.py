"""You are given two 2D integer arrays nums1 and nums2.

nums1[i] = [idi, vali] indicate that the number with the id idi has a value equal to vali.
nums2[i] = [idi, vali] indicate that the number with the id idi has a value equal to vali.
Each array contains unique ids and is sorted in ascending order by id.

Merge the two arrays into one array that is sorted in ascending order by id, respecting the following conditions:

Only ids that appear in at least one of the two arrays should be included in the resulting array.
Each id should be included only once and its value should be the sum of the values of this id in the two arrays. 
If the id does not exist in one of the two arrays then its value in that array is considered to be 0.
Return the resulting array. The returned array must be sorted in ascending order by id."""


class Solution:
    def mergeArrays(self, nums1: list[list[int]], nums2: list[list[int]]) -> list[list[int]]:
        nums1.extend(nums2)
        nums1.sort()
        keys, merged_lists = [], {}

        for sublist in nums1:
            key = sublist[0]
            values = sublist[1:]     
            if key in merged_lists:
                merged_lists[key] = [prev_val + new_val for prev_val, new_val in zip(merged_lists[key], values)]
            else:
                merged_lists[key] = values[:]           
            if key not in keys:
                keys.append(key)
        
        result = [[key] + merged_lists[key] for key in keys]
        return result
        

    
print(Solution().mergeArrays(nums1 = [[1,2],[2,3],[4,5]], nums2 = [[1,4],[3,2],[4,1]]))