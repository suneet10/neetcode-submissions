class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        s = list(s)
        arr = [0] * len(s)
        mans = 0
        dic = {}
        ans = 0
        for i in range(len(s)):
            # print(s[i],dic)

            if s[i] not in dic:
                dic[s[i]] = i
                ans += 1

            else:
                ans -= arr[dic[s[i]]]
                ans += 1

            arr[i] += ans
            mans = max(mans,ans)


            # else:
            #     # mans = max(mans,ans)
            #     # del dic[s[i]]
            #     # ans -= 1
        return mans
