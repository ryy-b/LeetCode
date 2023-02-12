#
# @lc app=leetcode id=14 lang=python3
#
# [14] Longest Common Prefix
#


# @lc code=start
class Solution:

    def longestCommonPrefix(self, strs: List[str]) -> str:

        n = min(list(map(lambda x: len(x), strs)))
        IS_COMMON = True

        ans = []
        for j in range(n):
            n_of_common_char = (len(set([t[j] for t in strs])))

            if n_of_common_char == 1:
                common_char = set([t[j] for t in strs]).pop()
                ans.append(common_char)

            else:
                IS_COMMON = False

            if not IS_COMMON:
                break

        return "".join(ans)


# @lc code=end
