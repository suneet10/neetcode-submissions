class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        s = list(s)
        mans = 0
        for i in range(len(s)):
            j = i
            ans = 0
            dic = {}
            while j< len(s) and s[j] not in dic:
                dic[s[j]] = 1
                ans += 1
                j += 1

            mans = max(mans,ans)

        return mans
