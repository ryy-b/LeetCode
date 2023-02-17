#
# @lc app=leetcode id=5 lang=python3
#
# [5] Longest Palindromic Substring
#

# @lc code=start
class Solution:
    def longestPalindrome(self, s: str) -> str:

        s_inverse = s[::-1]

        n = len(s)
        common_idx = []
        for i in range(n):
            if s[i] == s_inverse[i]:
                common_idx.append(i)

        if common_idx == []:
            return s[0]

        ans = ""
        for idx in common_idx:
            ans += s[idx]

        return ans

        
# @lc code=end

