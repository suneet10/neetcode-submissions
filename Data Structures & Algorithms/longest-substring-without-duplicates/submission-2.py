class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        s = list(s)
        mans = 0
        dic = {}
        ans = 0
        for i in range(len(s)):

            if s[i] not in dic:
                dic[s[i]] = 1
                ans += 1

            else:
                mans = max(mans,ans)
                dic = {}
                ans = 0

        mans = max(mans,ans)
        return mans
