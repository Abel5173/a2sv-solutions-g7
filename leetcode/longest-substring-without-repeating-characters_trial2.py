class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l = ''
        l_cnt = 0
        max_l = 0
        for i in range(len(s)):
            if s[i] not in l:
                l += s[i]
                l_cnt += 1
                max_l = max(l_cnt, max_l)
            else:
                l = s[i]
                l_cnt = 1
        return max_l