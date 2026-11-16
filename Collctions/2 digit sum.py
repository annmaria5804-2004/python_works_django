# You are given an array of integers nums and an integer target, return indices of the
#  two numbers such that they add up to target.

# You may assume that each input would have exactly one solution,
#  and you may not use the same element twice.

#  Example 1:

# Input: nums = [2,7,11,15], target = 9

# Output: [0,1]

nums = [2, 7, 11, 15] # [2,7][2,11][2,15][7,11][7,15].....[11,15]
                    # [2] [7,11,15 ]     [7] [11,15]       [11] [15]
                    # i=0  j=1,2,3
target = 9
for i in range(len(nums)): # range(0,4) i =0,1,2,3
    for j in range(i + 1, len(nums)): # range(1,4) 1,2,3
        if nums[i] + nums[j] == target:
            print([i, j])



# Explanation
# 1. len(nums) gives the number of elements in the list (4).
# 2. range(len(nums)) gives the indices 0, 1, 2, 3.
# 3. The inner loop starts from i + 1 so that we don't use the same element twice or check the same pair again.
# 4. nums[i] + nums[j] == target checks whether the two numbers add up to 9.
# 5. print([i, j]) displays the indices of the matching numbers.
# For the example:
# - nums[0] = 2
# - nums[1] = 7
# - 2 + 7 = 9
# Therefore, the answer is [0, 1].

# Remember: The question asks for the indices (positions), not the numbers themselves.