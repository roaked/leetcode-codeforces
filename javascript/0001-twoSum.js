/**
 * @param {number[]} nums
 * @param {number} target
 * @return {number[]}
 */
var twoSum = function(nums, target) {

    if (nums.length >= 2)
    {
        let i = 0;
        for (i = 0; i <= nums.length; i++)
        {
            for (j = 1; j <= nums.length-1; j++)
            {   
                if(i == j)
                {
                    continue

                }
                if (nums[i]+nums[j] == target)
                    {
                        return [i, j]

                    }


            }
        }
    }

};
