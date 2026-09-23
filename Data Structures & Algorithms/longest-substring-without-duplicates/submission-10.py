class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        s = list(s)
        left = 0
        ans = mans = 0
        dic = {}

        for i in range(len(s)):

            if s[i] not in dic:
                dic[s[i]] = i

            else:
                if dic[s[i]] > i - ans - 1:
                    left = dic[s[i]] + 1
                dic[s[i]] = i

            ans = (i-left) + 1
            mans = max(mans,ans)

        return mans