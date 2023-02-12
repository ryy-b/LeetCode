#
# @lc app=leetcode id=13 lang=python3
#
# [13] Roman to Integer
#


# @lc code=start
class Solution:

    def romanToInt(self, s: str) -> int:

        symbol_val_dict = {
            "I": 1,
            "V": 5,
            "X": 10,
            "L": 50,
            "C": 100,
            "D": 500,
            "M": 1000
        }

        ans = 0
        diff = 0
        for symbol in s:
            ans += symbol_val_dict[symbol]

        if "IV" in s or "IX" in s:
            diff -= 2

        if "XL" in s or "XC" in s:
            diff -= 20

        if "CD" in s or "CM" in s:
            diff -= 200

        return ans + diff


# @lc code=end
