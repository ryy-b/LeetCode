#
# @lc app=leetcode id=1 lang=python3
#
# [1] Two Sum
#


# @lc code=start
class Solution:

    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashmap = {}
        for i, num in enumerate(nums):
            search_value = target - num
            if search_value in hashmap:
                return sorted([i, hashmap[search_value]])

            else:
                hashmap[num] = i


# @lc code=end
