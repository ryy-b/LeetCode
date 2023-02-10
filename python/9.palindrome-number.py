#
# @lc app=leetcode id=9 lang=python3
#
# [9] Palindrome Number
#


# @lc code=start
class Solution:

    def isPalindrome(self, x: int) -> bool:

        str_x = str(x)

        if str_x == str_x[::-1]:
            return True
        else:
            return False


# @lc code=end
